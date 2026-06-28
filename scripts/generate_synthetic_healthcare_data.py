#!/usr/bin/env python3
"""Generate synthetic healthcare and IoT datasets for the project POC."""

from __future__ import annotations

import csv
import json
import random
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path


DEPARTMENTS = ["Emergency", "Cardiology", "ICU", "Radiology", "Outpatient"]
DEVICE_TYPES = ["Heart Rate Monitor", "Pulse Oximeter", "Thermometer", "Blood Pressure Cuff"]
STATUSES = ["admitted", "discharged", "under_observation"]


@dataclass(frozen=True)
class Paths:
    root: Path

    @property
    def raw(self) -> Path:
        return self.root / "data" / "bronze"

    @property
    def silver(self) -> Path:
        return self.root / "data" / "silver"

    @property
    def gold(self) -> Path:
        return self.root / "data" / "gold"


def ensure_directories(paths: Paths) -> None:
    for target in (paths.raw, paths.silver, paths.gold):
        target.mkdir(parents=True, exist_ok=True)


def daterange(start: date, days: int):
    for offset in range(days):
        yield start + timedelta(days=offset)


def generate_patients(seed: int, patient_count: int):
    random.seed(seed)
    patients = []
    for index in range(1, patient_count + 1):
        age = random.randint(18, 89)
        department = random.choice(DEPARTMENTS)
        status = random.choice(STATUSES)
        patients.append(
            {
                "patient_id": f"P{index:04d}",
                "age": age,
                "department": department,
                "status": status,
                "risk_score": round(random.uniform(0.05, 0.98), 3),
            }
        )
    return patients


def generate_events(seed: int, patients, days: int):
    random.seed(seed)
    events = []
    base_date = date(2026, 1, 1)
    event_id = 1
    for current_date in daterange(base_date, days):
        for patient in patients:
            arrival_minutes = random.randint(0, 1440)
            wait_time = random.randint(5, 180)
            occupancy = random.randint(40, 98)
            systolic = random.randint(95, 170)
            diastolic = random.randint(60, 110)
            heart_rate = random.randint(55, 135)
            events.append(
                {
                    "event_id": f"E{event_id:05d}",
                    "event_date": current_date.isoformat(),
                    "patient_id": patient["patient_id"],
                    "department": patient["department"],
                    "arrival_time": f"{arrival_minutes // 60:02d}:{arrival_minutes % 60:02d}",
                    "wait_minutes": wait_time,
                    "occupancy_pct": occupancy,
                    "systolic": systolic,
                    "diastolic": diastolic,
                    "heart_rate": heart_rate,
                }
            )
            event_id += 1
    return events


def generate_device_readings(seed: int, patients, days: int):
    random.seed(seed)
    readings = []
    base_date = date(2026, 1, 1)
    reading_id = 1
    for current_date in daterange(base_date, days):
        for patient in patients:
            if random.random() < 0.35:
                device = random.choice(DEVICE_TYPES)
                value = round(random.uniform(36.0, 102.0), 1)
                readings.append(
                    {
                        "reading_id": f"R{reading_id:05d}",
                        "event_date": current_date.isoformat(),
                        "patient_id": patient["patient_id"],
                        "device_type": device,
                        "reading_value": value,
                        "unit": "bpm" if "Heart" in device else "c",
                    }
                )
                reading_id += 1
    return readings


def aggregate_metrics(events):
    by_department = defaultdict(lambda: {"count": 0, "wait_total": 0, "occupancy_total": 0})
    by_date = defaultdict(lambda: {"count": 0, "wait_total": 0})

    for event in events:
        department_stats = by_department[event["department"]]
        department_stats["count"] += 1
        department_stats["wait_total"] += event["wait_minutes"]
        department_stats["occupancy_total"] += event["occupancy_pct"]

        day_stats = by_date[event["event_date"]]
        day_stats["count"] += 1
        day_stats["wait_total"] += event["wait_minutes"]

    rows = []
    for department, stats in sorted(by_department.items()):
        rows.append(
            {
                "department": department,
                "encounters": stats["count"],
                "avg_wait_minutes": round(stats["wait_total"] / stats["count"], 2),
                "avg_occupancy_pct": round(stats["occupancy_total"] / stats["count"], 2),
            }
        )

    return rows, by_date


def write_csv(path: Path, rows) -> None:
    if not rows:
        raise ValueError(f"No rows supplied for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, rows) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(rows, handle, indent=2)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    paths = Paths(root=root)
    ensure_directories(paths)

    patients = generate_patients(seed=7, patient_count=60)
    events = generate_events(seed=21, patients=patients, days=14)
    readings = generate_device_readings(seed=84, patients=patients, days=14)
    kpis, date_stats = aggregate_metrics(events)

    write_csv(paths.raw / "patients.csv", patients)
    write_csv(paths.raw / "clinical_events.csv", events)
    write_csv(paths.raw / "iot_readings.csv", readings)
    write_csv(paths.silver / "patient_events_clean.csv", events)
    write_csv(paths.gold / "department_kpis.csv", kpis)
    write_json(paths.gold / "daily_wait_stats.json", date_stats)

    print(f"Generated {len(patients)} patients")
    print(f"Generated {len(events)} clinical events")
    print(f"Generated {len(readings)} IoT readings")


if __name__ == "__main__":
    main()