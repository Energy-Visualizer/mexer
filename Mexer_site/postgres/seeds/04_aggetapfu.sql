-- Sample filler data for public."AggEtaPFU"
-- Generated on 2025-12-01
-- Contains 24 rows covering a variety of Dataset/Year/Country/Method combinations

BEGIN;

INSERT INTO public."AggEtaPFU" (
	"Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method",
	"EnergyType", "LastStage", "IncludesNEU", "Year", "ChoppedMat",
	"ChoppedVar", "ProductAggregation", "IndustryAggregation", "GrossNet",
	"EXp", "EXf", "EXu", "etapf", "etafu", "etapu"
) VALUES
	(1, 1, 1, 1, 1, 1, 1, 1, 1990, 1, 1, 1, 1, 1, 1000.0, 950.0, 50.0, 0.88, 0.85, 0.05),
	(1, 1, 1, 1, 2, 2, 1, 1, 2000, 1, 1, 2, 1, 1, 800.0, 760.0, 40.0, 0.86, 0.83, 0.05),
	(1, 1, 1, 2, 1, 1, 1, 1, 2010, 1, 1, 1, 2, 1, 1200.0, 1180.0, 20.0, 0.98, 0.98, 0.02);

-- Version range test data
INSERT INTO public."AggEtaPFU" (
    "Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method",
    "EnergyType", "LastStage", "IncludesNEU", "Year", "ChoppedMat",
    "ChoppedVar", "ProductAggregation", "IndustryAggregation", "GrossNet",
    "EXp", "EXf", "EXu", "etapf", "etafu", "etapu"
) VALUES
    (1, 1, 1,          1, 1, 1, 1, 1, 1800, 1, 1, 1, 1, 1, 100.0, 90.0, 10.0, 0.90, 0.89, 0.10),
    (1, 1, 2,          1, 1, 1, 1, 1, 1801, 1, 1, 1, 1, 1, 200.0, 180.0, 20.0, 0.91, 0.90, 0.10),
    (1, 2, 2147483647, 1, 1, 1, 1, 1, 1802, 1, 1, 1, 1, 1, 300.0, 270.0, 30.0, 0.92, 0.91, 0.10)
ON CONFLICT DO NOTHING;

COMMIT;

-- End of sample filler data for AggEtaPFU
