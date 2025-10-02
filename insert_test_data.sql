-- Lightweight test data for mexer database

BEGIN;

-- Lookup tables
INSERT INTO public."Dataset" ("DatasetID", "Dataset", "Public", "FullName", "Description") VALUES
    (1, 'Test Dataset', true, 'Test Dataset Full Name', 'This is a test dataset for unit testing purposes.'),
    (2, 'Another Dataset', false, 'Another Dataset Full Name', 'This is another dataset for testing.');

INSERT INTO public."Version" ("VersionID", "Version", "ReleaseDate", "Public", "ChangeNotes") VALUES
    (1, 1, '2023-01-01', true, 'Initial release of the test dataset.'),
    (2, 2, '2023-06-01', false, 'Second version with minor updates.');

INSERT INTO public."Country" ("CountryID", "Country", "FullName", "Description", "IsCountry", "IsAggregation", "IsContinent") VALUES
    (1, 'US', 'United States', 'Country in North America', true, false, false),
    (2, 'EU', 'European Union', 'Aggregation of European countries', false, true, false),
    (3, 'Asia', 'Asia Continent', 'Continent in the Eastern Hemisphere', false, false, true);

INSERT INTO public."Method" ("MethodID", "Method", "FullName", "Description") VALUES
    (1, 'Method A', 'Full Name of Method A', 'Description of Method A'),
    (2, 'Method B', 'Full Name of Method B', 'Description of Method B');

INSERT INTO public."EnergyType" ("EnergyTypeID", "EnergyType", "FullName", "Description") VALUES
    (1, 'Electricity', 'Electricity Energy Type', 'Energy type related to electricity'),
    (2, 'Fossil Fuels', 'Fossil Fuels Energy Type', 'Energy type related to fossil fuels');

INSERT INTO public."ECCStage" ("ECCStageID", "ECCStage", "FullName", "Description") VALUES
    (1, 'Stage 1', 'Full Name of Stage 1', 'Description of Stage 1'),
    (2, 'Stage 2', 'Full Name of Stage 2', 'Description of Stage 2');

INSERT INTO public."IncludesNEU" ("IncludesNEUID", "IncludesNEU", "FullName", "Description") VALUES
    (1, true, 'Includes Non-Energy Use', 'Data includes non-energy use'),
    (2, false, 'Excludes Non-Energy Use', 'Data excludes non-energy use');

INSERT INTO public."Year" ("YearID", "Year") VALUES
    (1, 2020),
    (2, 2021),
    (3, 2022);

INSERT INTO public."matname" ("matnameID", matname, "FullName", "Public", "Description", "RowFormat", "ColFormat") VALUES
    (1, 'Matrix A', 'Full Name of Matrix A', true, 'Description of Matrix A', 'Row Format A', 'Column Format A'),
    (2, 'Matrix B', 'Full Name of Matrix B', false, 'Description of Matrix B', 'Row Format B', 'Column Format B');

INSERT INTO public."Index" ("IndexID", "Index", "Order", "SankeyColumn") VALUES
    (1, 'Index 1', 1, 1),
    (2, 'Index 2', 2, 2);

INSERT INTO public."AggLevel" ("AggLevelID", "AggLevel", "FullName", "Description") VALUES
    (1, 'Level 1', 'Full Name of Level 1', 'Description of Level 1'),
    (2, 'Level 2', 'Full Name of Level 2', 'Description of Level 2');

INSERT INTO public."GrossNet" ("GrossNetID", "GrossNet", "FullName", "Description") VALUES
    (1, 'Gross', 'Gross Energy', 'Energy data measured in gross terms'),
    (2, 'Net', 'Net Energy', 'Energy data measured in net terms');

-- Sample data: PSUT (small matrix entry)
-- Columns: Dataset, ValidFromVersion, ValidToVersion, Country, Method, EnergyType, LastStage, IncludesNEU, Year, matname, i, j, value
INSERT INTO public."PSUT"("Dataset","ValidFromVersion","ValidToVersion","Country","Method","EnergyType","LastStage","IncludesNEU","Year","matname","i","j","value") VALUES
 (1,1,1,1,1,1,1,1,1,1,1,1,10.0),
 (1,1,1,1,1,1,1,1,1,1,1,2,5.5);

COMMIT;
