from __future__ import annotations

import argparse
import csv

from api_client import ApiClient
from transform import normalize_records


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch and normalize JSON API records.")
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", default="api-output.csv")
    args = parser.parse_args()

    records = normalize_records(ApiClient().get_json(args.url))
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "email"])
        writer.writeheader()
        writer.writerows(records)
    print(f"Wrote {len(records)} records to {args.output}")


if __name__ == "__main__":
    main()
