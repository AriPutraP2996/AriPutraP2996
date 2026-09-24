import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from validator import validate


def test_detects_duplicate_and_invalid_rows():
    rows = [
        {"customer_id": "C1", "email": "a@example.com", "country": "ID", "revenue": "10"},
        {"customer_id": "C1", "email": "bad", "country": "", "revenue": "-1"},
    ]
    result = validate(rows)
    codes = {issue["code"] for issue in result["issues"]}
    assert result["valid"] is False
    assert {"duplicate", "invalid_email", "missing_value", "negative_value"} <= codes


def test_empty_dataset_is_invalid():
    result = validate([])
    assert result["valid"] is False
    assert result["issues"][0]["code"] == "empty_dataset"


def test_valid_dataset():
    result = validate([
        {"customer_id": "C1", "email": "a@example.com", "country": "ID", "revenue": "10"},
        {"customer_id": "C2", "email": "b@example.com", "country": "MY", "revenue": "20"},
    ])
    assert result["valid"] is True
    assert result["issue_count"] == 0
