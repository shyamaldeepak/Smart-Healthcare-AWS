# Implementation Guide

## 1. Prepare the S3 layout

Create a single bucket and organize it into these prefixes:

- `bronze/` for raw CSV or JSON uploads
- `silver/` for cleaned and standardized records
- `gold/` for dashboard-ready aggregates
- `scripts/` for Glue and query artifacts

## 2. Generate synthetic data

Run the generator script to create reproducible healthcare datasets.

Expected outputs:

- `data/bronze/patients.csv`
- `data/bronze/clinical_events.csv`
- `data/bronze/iot_readings.csv`
- `data/silver/patient_events_clean.csv`
- `data/gold/department_kpis.csv`
- `data/gold/daily_wait_stats.json`

## 3. Configure AWS Glue

Use one crawler to scan the bronze prefix and build the first tables in the Glue Data Catalog.

Use one Glue ETL job to:

- read raw clinical events from S3
- cast numeric and date fields
- drop malformed records
- partition outputs by date and department
- write Parquet to silver and gold prefixes

## 4. Query with Athena

Create an Athena database and point it at the Glue Catalog tables.

Use the SQL in [sql/athena_queries.sql](../sql/athena_queries.sql) to explore:

- departmental workload
- daily wait time trends
- operational status bands

## 5. Build the dashboard

Connect Athena or the curated S3 gold zone to QuickSight or OpenSearch Dashboards.

Recommended visual tiles:

- average wait time by department
- occupancy trend over time
- critical alerts by day
- patient event volume by hour

## 6. Demo flow

1. Generate sample data.
2. Upload it to the bronze zone.
3. Run the Glue ETL job.
4. Refresh the Glue crawler.
5. Execute the Athena queries.
6. Present the dashboard metrics and summarize findings.

## 7. Deployment checklist

Use [docs/deployment-checklist.md](deployment-checklist.md) to verify the AWS setup before presenting the project.