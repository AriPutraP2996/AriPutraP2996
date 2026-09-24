from __future__ import annotations

import csv
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


@dataclass
class ValidationIssue:
    row: int | None
    field: str | None
    code: str
    message: str


REQUIRED_COLUMNS = ["customer_id", "email", "country", "revenue"]


def load_csv(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate(rows: list[dict[str, str]]) -> dict[str, Any]:
    issues: list[ValidationIssue] = []
    if not rows:
        issues.append(ValidationIssue(None, None, "empty_dataset", "Dataset contains no rows."))
        return {"valid": False, "row_count": 0, "issues": [asdict(i) for i in issues]}

    missing = [c for c in REQUIRED_COLUMNS if c not in rows[0]]
    for column in missing:
        issues.append(ValidationIssue(None, column, "missing_column", f"Required column '{column}' is missing."))

    if missing:
        return {"valid": False, "row_count": len(rows), "issues": [asdict(i) for i in issues]}

    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        customer_id = row["customer_id"].strip()
        email = row["email"].strip()
        country = row["country"].strip()
        revenue = row["revenue"].strip()

        if not customer_id:
            issues.append(ValidationIssue(index, "customer_id", "missing_value", "Customer ID is empty."))
        elif customer_id in seen:
            issues.append(ValidationIssue(index, "customer_id", "duplicate", f"Duplicate customer ID: {customer_id}."))
        seen.add(customer_id)

        if not email:
            issues.append(ValidationIssue(index, "email", "missing_value", "Email is empty."))
        elif "@" not in email or "." not in email.rsplit("@", 1)[-1]:
            issues.append(ValidationIssue(index, "email", "invalid_email", "Email format is invalid."))

        if not country:
            issues.append(ValidationIssue(index, "country", "missing_value", "Country is empty."))

        try:
            value = float(revenue)
            if value < 0:
                issues.append(ValidationIssue(index, "revenue", "negative_value", "Revenue cannot be negative."))
        except ValueError:
            issues.append(ValidationIssue(index, "revenue", "invalid_number", "Revenue must be numeric."))

    return {
        "valid": not issues,
        "row_count": len(rows),
        "issue_count": len(issues),
        "issues": [asdict(i) for i in issues],
    }
