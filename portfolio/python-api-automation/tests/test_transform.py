import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

import pytest
from transform import normalize_records


def test_normalizes_records():
    result = normalize_records([{"id": 7, "name": "  Ana  ", "email": "ANA@Example.COM"}])
    assert result == [{"id": 7, "name": "Ana", "email": "ana@example.com"}]


def test_rejects_non_array():
    with pytest.raises(ValueError, match="JSON array"):
        normalize_records({"id": 1})


def test_rejects_missing_required_field():
    with pytest.raises(ValueError, match="requires"):
        normalize_records([{"id": 1}])
