# Architecture

## Smart Hospital Operations Pipeline

```mermaid
flowchart LR
    A[Synthetic Patient Data\nCSV / JSON] --> B[Kinesis or Batch Upload]
    C[IoT Monitoring Events] --> B
    B --> D[S3 Bronze Zone]
    D --> E[Glue Crawler]
    E --> F[Glue ETL Job]
    F --> G[S3 Silver Zone\nCleaned Parquet]
    G --> H[S3 Gold Zone\nAnalytics Ready]
    H --> I[Athena SQL]
    H --> J[QuickSight or OpenSearch Dashboards]
    I --> J
    F --> K[Glue Data Catalog]
    K --> I
```

## Design Notes

- Bronze stores raw source records with minimal changes.
- Silver contains standardized, validated, and typed records.
- Gold contains aggregated KPIs ready for dashboard consumption.
- Athena is used for serverless SQL analytics to stay within Free Tier constraints.
- Glue provides both schema discovery and ETL orchestration.

## Target Use Case

The POC focuses on a smart hospital operations dashboard that tracks:

- patient arrivals and admissions
- wait-time trends by department
- IoT vital-sign alerts
- occupancy pressure and utilization