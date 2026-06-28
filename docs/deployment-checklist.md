# Deployment Checklist

## AWS Resources

- one S3 bucket for the data lake
- one Glue crawler for bronze data discovery
- one Glue ETL job for cleansing and Parquet output
- one Athena database for SQL analytics
- one dashboard tool such as QuickSight or OpenSearch Dashboards

## Pre-Deployment Checks

- synthetic data generated locally
- bucket prefixes created for bronze, silver, and gold
- Glue IAM role has access to the bucket
- Athena workgroup configured for the project
- Glue Data Catalog tables created by the crawler

## Run Order

1. Upload raw files to the bronze prefix.
2. Run the crawler to register the source schema.
3. Execute the Glue ETL job.
4. Refresh Athena tables.
5. Run the analytics queries.
6. Publish or screenshot dashboard visuals.

## Validation Checklist

- query row counts match the generated source data
- department KPI query returns one row per department
- alert query returns only high wait-time services
- dashboard metrics align with the gold zone aggregates