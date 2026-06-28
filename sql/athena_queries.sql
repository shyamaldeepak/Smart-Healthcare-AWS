-- Athena analytics queries for the smart healthcare POC

SELECT
  department,
  COUNT(*) AS encounters,
  ROUND(AVG(wait_minutes), 2) AS avg_wait_minutes,
  ROUND(AVG(occupancy_pct), 2) AS avg_occupancy_pct
FROM clinical_events_clean
GROUP BY department
ORDER BY avg_wait_minutes DESC;

SELECT
  event_date,
  COUNT(*) AS daily_encounters,
  ROUND(AVG(wait_minutes), 2) AS avg_wait_minutes
FROM clinical_events_clean
GROUP BY event_date
ORDER BY event_date;

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