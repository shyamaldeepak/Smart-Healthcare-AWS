# Presentation Notes

## Opening

Explain that the project is a serverless smart-hospital analytics POC built on AWS Free Tier services.

## Demo Flow

1. Show the architecture diagram.
2. Run the synthetic data generator.
3. Show the validation output.
4. Walk through the Glue ETL job and Athena SQL.
5. Review the dashboard summary and sample insights.
6. Close with the AI extension ideas.

## Key Talking Points

- the design uses only one bucket and one Glue job to stay within the assignment constraints
- the dataset is synthetic and safe to share
- the gold zone is the source of truth for dashboard metrics
- the optional AI extension can be added without changing the data model