"""AWS Glue PySpark job for the smart healthcare pipeline POC.

This script is intentionally written to match the shape of a real Glue job.
It reads raw CSV data from S3, standardizes the schema, and writes Parquet
outputs to the silver and gold zones.
"""

import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as F


args = getResolvedOptions(
    sys.argv,
    ["JOB_NAME", "SOURCE_PATH", "SILVER_PATH", "GOLD_PATH"],
)

sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

raw_events = spark.read.option("header", "true").csv(args["SOURCE_PATH"] + "/clinical_events.csv")

clean_events = (
    raw_events.select(
        F.col("event_id"),
        F.to_date("event_date").alias("event_date"),
        F.col("patient_id"),
        F.col("department"),
        F.col("arrival_time"),
        F.col("wait_minutes").cast("int"),
        F.col("occupancy_pct").cast("int"),
        F.col("systolic").cast("int"),
        F.col("diastolic").cast("int"),
        F.col("heart_rate").cast("int"),
    )
    .dropna(subset=["event_id", "event_date", "patient_id"])
)

department_kpis = (
    clean_events.groupBy("department")
    .agg(
        F.count("event_id").alias("encounters"),
        F.round(F.avg("wait_minutes"), 2).alias("avg_wait_minutes"),
        F.round(F.avg("occupancy_pct"), 2).alias("avg_occupancy_pct"),
    )
)

clean_events.write.mode("overwrite").partitionBy("event_date", "department").parquet(args["SILVER_PATH"] + "/clinical_events")
department_kpis.write.mode("overwrite").parquet(args["GOLD_PATH"] + "/department_kpis")

job.commit()