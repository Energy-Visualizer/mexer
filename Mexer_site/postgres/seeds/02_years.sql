-- Years seed (seed 02)
-- Use generate_series to insert years from 1..2025
INSERT INTO public."Year" ("YearID", "Year")
SELECT gs, gs FROM generate_series(1, 2025) AS gs
ON CONFLICT DO NOTHING;
