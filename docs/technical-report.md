# Technical Report

## 1. Objective

This project demonstrates a serverless AWS data and analytics pipeline for smart healthcare operations. The goal is to transform synthetic clinical and IoT data into curated insights that can support operational decisions without relying on non-Free-Tier infrastructure.

## 2. Architecture Summary

The design follows a bronze-silver-gold data lake pattern:

- Bronze stores raw uploaded patient and device data.
- Silver stores standardized, validated, and partitioned records.
- Gold stores aggregated business metrics for analytics and dashboards.

AWS Glue handles ingestion, schema management, and ETL. Athena provides serverless SQL access to the curated datasets. QuickSight or OpenSearch Dashboards can visualize the results.

## 3. Data Strategy

The project uses synthetic data only. This keeps the POC privacy-safe while still allowing realistic operational patterns:

- patient attributes such as age, status, and risk score
- clinical events such as wait time, occupancy, and vitals
- IoT readings such as heart rate and temperature-like measurements

The sample generator produces a repeatable dataset so the pipeline is deterministic and easy to review.

## 4. ETL and Analytics

The Glue ETL job cleans the raw event data by:

- enforcing types for numeric fields
- parsing event dates
- dropping malformed rows
- writing partitioned Parquet to silver and gold zones

Athena queries calculate:

- average wait time by department
- daily encounter volume
- operational status bands

The dashboard summary shows a clear pattern: outpatient and radiology have the highest encounter volumes and longest waits, while emergency shows the highest occupancy pressure.

## 5. Challenges and Limitations

The main limitation is that the project is a POC rather than a live cloud deployment. It does not include real Kinesis streams, Step Functions orchestration, or a deployed QuickSight dashboard in this repository.

Another limitation is that the local generator writes CSV and JSON sample outputs, while the Glue job is represented as a realistic AWS script that would write Parquet in the cloud environment.

## 6. Future Improvements

The next iteration could add:

- Kinesis streaming ingestion for near-real-time monitoring
- automatic Glue crawler and ETL orchestration through Step Functions
- anomaly detection for abnormal vitals or device readings
- patient admission forecasting using SageMaker or Athena ML
- a published QuickSight dashboard linked directly to Athena tables

## 7. Conclusion

The solution provides a complete, low-cost reference architecture for a smart hospital data platform. It is suitable as a course deliverable and as a starting point for more advanced AI and operational analytics work.