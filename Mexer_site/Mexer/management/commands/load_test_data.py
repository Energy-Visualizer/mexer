from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import DEFAULT_DB_ALIAS, connections, transaction


class Command(BaseCommand):
    help = "Load SQL seed files from postgres/seeds in alphabetical order."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dir",
            help="Directory containing seed SQL files",
            default="postgres/seeds",
        )
        parser.add_argument(
            "--database", help="Database alias to use", default=DEFAULT_DB_ALIAS
        )

    def handle(self, *args, **options):
        if not settings.IS_LOCAL:
            self.stderr.write(
                self.style.ERROR("This command can only be run in a local environment.")
            )
            raise CommandError("Not a local environment")

        seeds_dir = Path(options["dir"])
        if not seeds_dir.exists():
            self.stderr.write(
                self.style.ERROR(f"Seeds directory not found: {seeds_dir}")
            )
            raise CommandError("Seeds directory not found")

        sql_files = sorted(seeds_dir.glob("*.sql"))
        if not sql_files:
            self.stdout.write(
                self.style.WARNING("No .sql files found in seeds directory.")
            )
            return

        conn = connections[options["database"]]

        with transaction.atomic(), conn.cursor() as cursor:
            for sql_file in sql_files:
                self.stdout.write(f"Loading: {sql_file}")
                sql_text = sql_file.read_text()
                try:
                    cursor.execute(sql_text)
                except Exception as e:
                    self.stderr.write(
                        self.style.ERROR(f"Error executing {sql_file}: {e}")
                    )
                    raise

        self.stdout.write(self.style.SUCCESS("Seed files loaded successfully."))
