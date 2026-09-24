# Data Quality & Validation

A deterministic Python workflow for profiling and validating tabular business data before downstream analysis.

## What it demonstrates
- schema and required-column validation
- missing-value checks
- duplicate detection
- basic type/format validation
- numeric range validation
- JSON quality report
- automated tests

## Run
```bash
python portfolio/data-quality-validation/run_validation.py
python -m pytest portfolio/data-quality-validation/tests -q
```

The sample dataset is intentionally small and synthetic so the workflow is reproducible and does not depend on private data.
