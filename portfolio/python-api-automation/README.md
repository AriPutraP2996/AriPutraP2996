# Python API Automation

A small, testable API-ingestion workflow that retrieves JSON records, normalizes them into a stable schema, and writes a CSV artifact.

## What it demonstrates
- HTTP client abstraction
- timeout-aware requests
- response validation
- JSON-to-CSV normalization
- deterministic tests without network access
- CLI execution

## Run
```bash
python portfolio/python-api-automation/run_pipeline.py
python -m pytest portfolio/python-api-automation/tests -q
```

Tests use a fake HTTP client, so CI does not depend on a live external service.
