-- Lookup tables (seed 01)

BEGIN;

-- Dataset
INSERT INTO public."Dataset" ("DatasetID", "Dataset", "Public", "FullName", "Description") VALUES
    (1, 'Test Dataset', true, 'Test Dataset Full Name', 'This is a test dataset for unit testing purposes.'),
    (2, 'Another Dataset', false, 'Another Dataset Full Name', 'This is another dataset for testing.')
ON CONFLICT DO NOTHING;

-- Version
INSERT INTO public."Version" ("VersionID", "Version", "ReleaseDate", "Public", "ChangeNotes") VALUES
    (1, 1, '2023-01-01', true, 'Initial release of the test dataset.'),
    (2, 2, '2023-06-01', false, 'Second version with minor updates.'),
    (2147483647, 2147483647, '9999-12-31', true, 'Sentinel version representing open-ended validity.')
ON CONFLICT DO NOTHING;

-- Country
INSERT INTO public."Country" ("CountryID", "Country", "FullName", "Description", "IsCountry", "IsAggregation", "IsContinent") VALUES
    (1, 'US', 'United States', 'Country in North America', true, false, false),
    (2, 'EU', 'European Union', 'Aggregation of European countries', false, true, false),
    (3, 'Asia', 'Asia Continent', 'Continent in the Eastern Hemisphere', false, false, true)
ON CONFLICT DO NOTHING;

-- Method
INSERT INTO public."Method" ("MethodID", "Method", "FullName", "Description") VALUES
    (1, 'Method A', 'Full Name of Method A', 'Description of Method A'),
    (2, 'Method B', 'Full Name of Method B', 'Description of Method B')
ON CONFLICT DO NOTHING;

-- EnergyType
INSERT INTO public."EnergyType" ("EnergyTypeID", "EnergyType", "FullName", "Description") VALUES
    (1, 'Energy', 'Energy', 'Energy type related to electricity'),
    (2, 'Exergy', 'Exergy', 'Energy type related to fossil fuels')
ON CONFLICT DO NOTHING;

-- ECCStage
INSERT INTO public."ECCStage" ("ECCStageID", "ECCStage", "FullName", "Description") VALUES
    (1, 'Stage 1', 'Full Name of Stage 1', 'Description of Stage 1'),
    (2, 'Stage 2', 'Full Name of Stage 2', 'Description of Stage 2')
ON CONFLICT DO NOTHING;

-- IncludesNEU
INSERT INTO public."IncludesNEU" ("IncludesNEUID", "IncludesNEU", "FullName", "Description") VALUES
    (1, true, 'Includes Non-Energy Use', 'Data includes non-energy use'),
    (2, false, 'Excludes Non-Energy Use', 'Data excludes non-energy use')
ON CONFLICT DO NOTHING;

-- matname, Index, AggLevel, GrossNet
INSERT INTO public."matname" ("matnameID", matname, "FullName", "Public", "Description", "RowFormat", "ColFormat") VALUES
    (1, 'R', 'R', true, 'Description of Matrix R', '', ''),
    (2, 'U', 'U', false, 'Description of Matrix U', '', ''),
    (3, 'V', 'V', false, 'Description of Matrix V', '', ''),
    (4, 'Y', 'Y', false, 'Description of Matrix Y', '', '')
ON CONFLICT DO NOTHING;

INSERT INTO public."Index" ("IndexID", "Index", "Order", "SankeyColumn") VALUES
    (1, 'Index 1', 1, 1),
    (2, 'Index 2', 2, 2)
ON CONFLICT DO NOTHING;

INSERT INTO public."AggLevel" ("AggLevelID", "AggLevel", "FullName", "Description") VALUES
    (1, 'Level 1', 'Full Name of Level 1', 'Description of Level 1'),
    (2, 'Level 2', 'Full Name of Level 2', 'Description of Level 2')
ON CONFLICT DO NOTHING;

INSERT INTO public."GrossNet" ("GrossNetID", "GrossNet", "FullName", "Description") VALUES
    (1, 'Gross', 'Gross Energy', 'Energy data measured in gross terms'),
    (2, 'Net', 'Net Energy', 'Energy data measured in net terms')
ON CONFLICT DO NOTHING;

COMMIT;
