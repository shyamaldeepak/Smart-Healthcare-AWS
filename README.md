# Smart Healthcare AWS

This repository contains a complete proof-of-concept for the Cloud Computing and Big Data S3 final project.

## Project Scope

The solution models a smart-hospital analytics pipeline on AWS Free Tier services:

- Synthetic healthcare and IoT data generation
- S3 data lake layout with bronze, silver, and gold zones
- Glue ETL job for cleansing and Parquet conversion
- Athena SQL for operational analytics
- Dashboard and reporting artifacts for decision support

## Repository Contents

- [Architecture](docs/architecture.md)
- [Data Model](docs/data-model.md)
- [Implementation Guide](docs/implementation-guide.md)
- [Dashboard Summary](docs/dashboard-summary.md)
- [Sample Insights](docs/sample-insights.md)
- [Technical Report](docs/technical-report.md)
- [Optional AI Extension](docs/ai-extension.md)
- [Presentation Notes](docs/presentation-notes.md)
- [Final Review Checklist](docs/final-review-checklist.md)
- [Synthetic Data Generator](scripts/generate_synthetic_healthcare_data.py)
- [Glue ETL Job](glue_jobs/healthcare_etl_job.py)
- [Athena Queries](sql/athena_queries.sql)
- [Validation Script](scripts/validate_outputs.py)

## Recommended Workflow

1. Generate synthetic healthcare and IoT data.
2. Upload raw data to S3 bronze storage.
3. Run the Glue ETL job to produce cleaned silver and gold datasets.
4. Register the Glue Data Catalog tables.
5. Query the curated datasets in Athena.
6. Present the dashboard metrics and findings.

## Local Quickstart

```bash
python scripts/generate_synthetic_healthcare_data.py
python scripts/analytics_demo.py
```

## Submission Checklist

- architecture diagram
- implementation guide
- demo script or notebook
- dashboard summary
- technical report