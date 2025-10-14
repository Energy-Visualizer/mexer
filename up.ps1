<#
Windows-friendly PowerShell script to bring up the development stack.

Notes / Assumptions:
- Assumes Docker Desktop is installed and available in PATH.
- For Windows this script will convert host paths to a Docker-friendly form
  where appropriate and will avoid requiring a host `psql` by running the
  SQL import inside the Postgres container.
- Run from the project root (where `.env`, `Mexer_site`, and `postgres/` live).
#>

$ErrorActionPreference = 'Stop'

$isWindows = $IsWindows

function Convert-ToDockerPath {
  param([string]$Path)
  if (-not (Test-Path $Path)) { throw "Path not found: $Path" }
  $resolved = (Resolve-Path $Path).ProviderPath

  if ($isWindows) {
    # Convert C:\foo\bar -> /c/foo/bar so Docker (and WSL paths) accept it
    $p = $resolved -replace '\\','/'
    if ($p -match '^([A-Za-z]):/(.*)') { $p = "/$($matches[1].ToLower())/$($matches[2])" }
    return $p
  }
  else { return $resolved }
}

function Ensure-DockerNetwork($name) {
  try { docker network inspect $name | Out-Null; Write-Host "Docker network '$name' exists." }
  catch { Write-Host "Creating Docker network '$name'..."; docker network create $name }
}

Write-Host "Building image..."
docker build -t mexer .

Write-Host "Creating Docker network..."
Ensure-DockerNetwork mexerNetwork

Write-Host "Starting PostgreSQL Docker container..."
try { docker rm -f postgres | Out-Null } catch { }

$projectRoot = (Get-Location).Path
$schemaHostPath = Join-Path $projectRoot 'postgres\mexer_schema.sql'

if (-not (Test-Path $schemaHostPath)) {
  Write-Host "Schema file not found at $schemaHostPath" -ForegroundColor Red
  throw "Cannot continue without schema file."
}

$schemaDockerPath = if ($isWindows) { Convert-ToDockerPath $schemaHostPath } else { $schemaHostPath }

docker run -d --name postgres -p 5432:5432 `
  -e POSTGRES_USER=postgres `
  -e POSTGRES_PASSWORD=postgres `
  -v "$schemaDockerPath:/docker-entrypoint-initdb.d/mexer_schema.sql" `
  --network mexerNetwork `
  postgres

Write-Host "Waiting for PostgreSQL to be ready..."
while ($true) {
  & docker exec postgres pg_isready -U postgres >$null 2>$null
  if ($LASTEXITCODE -eq 0) { break }
  Start-Sleep -Seconds 1
}

Write-Host "Starting Mexer Docker container..."
try { docker rm -f mexer | Out-Null } catch { }

$mexerHostPath = Join-Path $projectRoot 'Mexer_site'
if (-not (Test-Path $mexerHostPath)) { throw "Missing Mexer_site directory: $mexerHostPath" }
$mexerDockerPath = if ($isWindows) { Convert-ToDockerPath $mexerHostPath } else { $mexerHostPath }

$wordsHost = '/usr/share/dict/words'
$wordsMountArg = ''
if ($isWindows) { $wordsHostExists = $false } else { $wordsHostExists = Test-Path $wordsHost }
if ($wordsHostExists) { $wordsMountArg = "-v $wordsHost:$wordsHost" }

$runArgs = @(
  '--name', 'mexer', '-dp', '8000:8000',
  '--env-file', '.env'
)

if ($wordsMountArg) { $runArgs += $wordsMountArg }
$runArgs += @('-v', "$mexerDockerPath:/app:rw", '--network', 'mexerNetwork', 'mexer', 'python3', 'manage.py', 'debug', '0.0.0.0:8000')

Write-Host "Running docker run for mexer..."
docker run $runArgs

Write-Host "Running Migrations..."
docker exec mexer python3 manage.py migrate

Write-Host "Inserting test data..."
$insertFile = Join-Path $projectRoot 'postgres\insert_test_data.sql'
if (-not (Test-Path $insertFile)) { Write-Host "Insert SQL not found at $insertFile" -ForegroundColor Yellow }
else {
  try {
    Write-Host "Copying test SQL into Postgres container..."
    docker cp "$insertFile" postgres:/tmp/insert_test_data.sql
    Write-Host "Executing SQL inside Postgres container..."
    docker exec -u postgres postgres psql -U postgres -f /tmp/insert_test_data.sql
  }
  catch {
    Write-Host "Failed to import via container psql: $_. Trying host psql as fallback..." -ForegroundColor Yellow
    if (Get-Command psql -ErrorAction SilentlyContinue) {
      & psql "postgresql://postgres:postgres@localhost" -f $insertFile
    }
    else { Write-Host "No psql found on host to use as fallback. Please import $insertFile manually." -ForegroundColor Red }
  }
}

Write-Host "Creating superuser..."
docker exec -it mexer bash -c 'python3 manage.py createsuperuser --noinput --username "$DJANGO_SUPERUSER_USERNAME" --email "$DJANGO_SUPERUSER_EMAIL"'

Write-Host "Done."
