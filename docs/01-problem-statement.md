# Problem Statement

## Context

In Tanzania, water points (boreholes, wells, and other sources) are critical infrastructure for rural communities. When pumps fail, communities lose access to clean water. Maintenance is expensive and resources are limited — so predicting pump status from available survey data is a high-value analytics problem.

## Objective

Build a machine learning classifier that predicts water point functionality from survey features recorded at each site.

## Target Variable

Three-class classification (`status_group`):

| Class | Meaning |
|-------|---------|
| `functional` | Pump is working |
| `functional needs repair` | Pump works but requires maintenance |
| `non functional` | Pump is not working |

## Dataset Source

- **Competition:** DrivenData — [Pump It Up: Data Mining the Water Table](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/)
- **Origin:** Taarifa / open water point data for Tanzania
- **Size:** ~59,000 labeled training records
- **Features:** ~40 survey fields per water point (geography, construction, management, water quality, etc.)

## Success Criteria

- Clean and merge raw training files into a modeling-ready dataset
- Explore feature distributions and relationships with pump status
- Train and evaluate a multi-class classifier
- Document methodology and results
