#!/usr/bin/env python3
"""Validate the generated sample outputs for the healthcare POC."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=None, help="Repository root containing the generated data folder")
    return parser


def load_csv(path: Path):
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    args = build_parser().parse_args()
    root = args.root or Path(__file__).resolve().parents[1]

    patients = load_csv(root / "data" / "bronze" / "patients.csv")
    events = load_csv(root / "data" / "bronze" / "clinical_events.csv")
    readings = load_csv(root / "data" / "bronze" / "iot_readings.csv")
    department_kpis = load_csv(root / "data" / "gold" / "department_kpis.csv")
    daily_stats = json.loads((root / "data" / "gold" / "daily_wait_stats.json").read_text(encoding="utf-8"))

    assert len(patients) > 0, "patients.csv is empty"
    assert len(events) > 0, "clinical_events.csv is empty"
    assert len(readings) > 0, "iot_readings.csv is empty"
    assert len(department_kpis) == 5, "department_kpis.csv should have one row per department"
    assert len(daily_stats) == 14, "daily_wait_stats.json should include 14 days"

    print("Validation passed")
    print(f"Patients: {len(patients)}")
    print(f"Events: {len(events)}")
    print(f"Readings: {len(readings)}")


if __name__ == "__main__":
    main()