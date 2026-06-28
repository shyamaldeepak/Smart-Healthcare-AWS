#!/usr/bin/env python3
"""Print a compact analytics summary from the generated gold datasets."""

from __future__ import annotations

import csv
import json
from pathlib import Path


def load_csv(path: Path):
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    department_kpis = load_csv(root / "data" / "gold" / "department_kpis.csv")
    daily_wait_stats = json.loads((root / "data" / "gold" / "daily_wait_stats.json").read_text(encoding="utf-8"))

    print("Department KPIs")
    for row in department_kpis:
        print(
            f"- {row['department']}: {row['encounters']} encounters, "
            f"avg wait {row['avg_wait_minutes']} minutes, "
            f"occupancy {row['avg_occupancy_pct']}%"
        )

    busiest_day, busiest_stats = max(daily_wait_stats.items(), key=lambda item: item[1]["count"])
    print()
    print(f"Busiest day: {busiest_day} with {busiest_stats['count']} encounters")


if __name__ == "__main__":
    main()