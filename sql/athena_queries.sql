-- Athena analytics queries for the smart healthcare POC

-- 1. Department workload summary

SELECT
  department,
  COUNT(*) AS encounters,
  ROUND(AVG(wait_minutes), 2) AS avg_wait_minutes,
  ROUND(AVG(occupancy_pct), 2) AS avg_occupancy_pct
FROM clinical_events_clean
GROUP BY department
ORDER BY avg_wait_minutes DESC;

-- 2. Daily throughput and wait trend

SELECT
  event_date,
  COUNT(*) AS daily_encounters,
  ROUND(AVG(wait_minutes), 2) AS avg_wait_minutes
FROM clinical_events_clean
GROUP BY event_date
ORDER BY event_date;

-- 3. Operational status bands for dashboard tiles

SELECT
  department,
  CASE
    WHEN avg_wait_minutes >= 90 THEN 'critical'
    WHEN avg_wait_minutes >= 60 THEN 'elevated'
    ELSE 'normal'
  END AS operational_status,
  avg_wait_minutes,
  avg_occupancy_pct
FROM department_kpis;

-- 4. Critical wait-time alert filter

SELECT
  event_date,
  department,
  avg_wait_minutes,
  avg_occupancy_pct
FROM department_kpis
WHERE avg_wait_minutes >= 90
ORDER BY avg_wait_minutes DESC;