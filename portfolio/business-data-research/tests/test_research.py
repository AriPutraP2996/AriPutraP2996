import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from research import prepare, summarize


def test_prepare_deduplicates_companies():
    rows = [
        {"company": " Alpha Labs ", "country": "ID", "industry": "Tech", "employees": "10"},
        {"company": "alpha labs", "country": "ID", "industry": "Tech", "employees": "10"},
    ]
    result = prepare(rows)
    assert len(result) == 1


def test_summary_is_reproducible():
    rows = prepare([
        {"company": "A", "country": "ID", "industry": "Tech", "employees": "10"},
        {"company": "B", "country": "MY", "industry": "Tech", "employees": "20"},
    ])
    result = summarize(rows)
    assert result["company_count"] == 2
    assert result["total_employees"] == 30
    assert result["average_employees"] == 15
