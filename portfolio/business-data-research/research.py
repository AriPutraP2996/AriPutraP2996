from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


REQUIRED = {"company", "country", "industry", "employees"}


def load(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def prepare(rows: list[dict[str, str]]) -> list[dict]:
    if rows and not REQUIRED.issubset(rows[0]):
        missing = REQUIRED - set(rows[0])
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")

    unique: dict[str, dict] = {}
    for row in rows:
        company = row["company"].strip()
        if not company:
            continue
        key = company.casefold()
        try:
            employees = int(row["employees"])
        except ValueError:
            continue
        unique[key] = {
            "company": company,
            "country": row["country"].strip(),
            "industry": row["industry"].strip(),
            "employees": employees,
        }
    return list(unique.values())


def summarize(rows: list[dict]) -> dict:
    industries = Counter(row["industry"] for row in rows)
    countries = Counter(row["country"] for row in rows)
    return {
        "company_count": len(rows),
        "total_employees": sum(row["employees"] for row in rows),
        "average_employees": round(sum(row["employees"] for row in rows) / len(rows), 2) if rows else 0,
        "top_industries": industries.most_common(),
        "countries": countries.most_common(),
    }
