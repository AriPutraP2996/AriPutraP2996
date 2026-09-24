# Business Data Research

A reproducible workflow for turning a small business dataset into a research-ready summary.

## Workflow
1. normalize text fields
2. remove duplicate entities
3. validate required fields
4. calculate simple business metrics
5. produce a Markdown research brief

The example uses synthetic business records. It demonstrates the workflow and QA logic without claiming real-world research results.

## Run
```bash
python portfolio/business-data-research/run_research.py
python -m pytest portfolio/business-data-research/tests -q
```
