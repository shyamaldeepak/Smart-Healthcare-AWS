# Data Model

## Bronze Zone

### patients.csv

- patient_id
- age
- department
- status
- risk_score

### clinical_events.csv

- event_id
- event_date
- patient_id
- department
- arrival_time
- wait_minutes
- occupancy_pct
- systolic
- diastolic
- heart_rate

### iot_readings.csv

- reading_id
- event_date
- patient_id
- device_type
- reading_value
- unit

## Silver Zone

The silver layer keeps the same clinical event structure after cleansing and type casting.

## Gold Zone

### department_kpis.csv

- department
- encounters
- avg_wait_minutes
- avg_occupancy_pct

### daily_wait_stats.json

- date key
- count
- wait_total

## Analytics Notes

The gold zone is the source of truth for dashboard visualizations and Athena summary queries.