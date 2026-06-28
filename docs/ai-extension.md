# Optional AI Extension

## Forecasting Use Case

The next step for this POC is a simple admission-rate forecast using historical event volume by day and department.

Possible approaches:

- SageMaker forecasting model
- Athena ML for SQL-first experimentation
- a lightweight anomaly score over rolling averages

## Anomaly Detection Use Case

The IoT readings can also support anomaly detection when values move outside expected ranges.

Potential signals:

- unusually high heart rate readings
- repeated readings that suggest device malfunction
- occupancy spikes that correlate with elevated wait times

## Why It Fits the Project

This extension stays aligned with the project brief because it uses the same synthetic datasets, the same S3 data lake layout, and the same dashboard-ready KPI outputs.