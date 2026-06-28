# Dashboard Summary

## Sample Dataset Snapshot

The generated proof-of-concept data includes:

- 60 synthetic patients
- 840 clinical events over 14 days
- 279 IoT readings

## Key Metrics

| Metric | Value |
| --- | --- |
| Average wait time | 92.73 minutes |
| Average occupancy | 69.27% |
| Maximum wait time | 180 minutes |
| Highest-volume department | Outpatient and Radiology |

## Department View

| Department | Encounters | Avg Wait | Avg Occupancy |
| --- | --- | --- | --- |
| Cardiology | 140 | 89.58 | 69.37% |
| Emergency | 154 | 90.77 | 71.96% |
| ICU | 126 | 89.95 | 68.75% |
| Outpatient | 210 | 95.54 | 67.24% |
| Radiology | 210 | 95.11 | 69.56% |

## Suggested Visual Tiles

- bar chart for average wait time by department
- line chart for daily average wait time
- heat map for occupancy pressure by day and department
- KPI cards for total encounters and critical wait-time threshold breaches

## Operational Insights

The sample data suggests that outpatient and radiology services carry the highest volume and also the longest average wait times. Emergency has the highest average occupancy, which makes it the most constrained service line in the snapshot.

These signals are good candidates for alerting logic in the dashboard and for follow-up forecasting in a later AI extension.