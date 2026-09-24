from __future__ import annotations

import argparse
from pathlib import Path

from research import load, prepare, summarize


def render(summary: dict) -> str:
    lines = [
        "# Business Data Research Brief",
        "",
        "## Summary",
        f"- Companies: {summary['company_count']}",
        f"- Total employees: {summary['total_employees']}",
        f"- Average employees per company: {summary['average_employees']}",
        "",
        "## Industry distribution",
    ]
    lines += [f"- {name}: {count}" for name, count in summary["top_industries"]]
    lines += ["", "## Country distribution"]
    lines += [f"- {name}: {count}" for name, count in summary["countries"]]
    lines += ["", "_Source: synthetic portfolio dataset; figures are reproducible from the checked-in CSV._"]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a business research brief.")
    parser.add_argument("--input", default=str(Path(__file__).parent / "data" / "companies.csv"))
    parser.add_argument("--output", default=str(Path(__file__).parent / "reports" / "research-brief.md"))
    args = parser.parse_args()

    summary = summarize(prepare(load(args.input)))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(summary), encoding="utf-8")
    print(render(summary))


if __name__ == "__main__":
    main()
