BEGIN;

-- PSUT sample data (seed 03)
-- Columns: Dataset, ValidFromVersion, ValidToVersion, Country, Method, EnergyType, LastStage, IncludesNEU, Year, matname, i, j, value
INSERT INTO public."PSUT"("Dataset","ValidFromVersion","ValidToVersion","Country","Method","EnergyType","LastStage","IncludesNEU","Year","matname","i","j","value") VALUES
 (1,1,1,1,1,1,1,1,1,1,1,1,10.0),
 (1,1,1,1,1,1,1,1,1,1,1,2,5.5)
ON CONFLICT DO NOTHING;

INSERT INTO public."PSUTReAllChopAllDsAllGrAll"("Dataset","ValidFromVersion","ValidToVersion","Country","Method","EnergyType","LastStage","IncludesNEU","Year","ChoppedMat","ChoppedVar","ProductAggregation","IndustryAggregation","matname","i","j","value") VALUES
 (1,1,1,1,1,1,1,1,2020,1,1,1,1,1,1,1,10.0),
 (1,1,1,1,1,1,1,1,2021,1,1,1,1,1,1,2,5.5)
ON CONFLICT DO NOTHING;

-- Version range test data
INSERT INTO public."PSUTReAllChopAllDsAllGrAll"("Dataset","ValidFromVersion","ValidToVersion","Country","Method","EnergyType","LastStage","IncludesNEU","Year","ChoppedMat","ChoppedVar","ProductAggregation","IndustryAggregation","matname","i","j","value") VALUES
 (1,1,1,1,1,1,1,1,2020,1,1,1,1,1,1,1,10.0),
 (1,1,1,1,1,1,1,1,2021,1,1,1,1,1,1,2,5.5),
 (1,1,1,          1,1,1,1,1,1800,1,1,1,1,1,1,1,11.0),
 (1,1,2,          1,1,1,1,1,1801,1,1,1,1,1,1,1,12.0),
 (1,2,2147483647, 1,1,1,1,1,1802,1,1,1,1,1,1,1,13.0)
ON CONFLICT DO NOTHING;

COMMIT;
