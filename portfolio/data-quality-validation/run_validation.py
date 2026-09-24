from __future__ import annotations

import argparse
import json
from pathlib import Path

from validator import load_csv, validate


ROOT = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a CSV dataset.")
    parser.add_argument("--input", default=str(ROOT / "data" / "customers.csv"))
    parser.add_argument("--output", default=str(ROOT / "reports" / "validation-report.json"))
    args = parser.parse_args()

    result = validate(load_csv(args.input))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
