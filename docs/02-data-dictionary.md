# Data Dictionary

Key features used in the AquaPredict pipeline. Full column list is in `data/training_values.csv`.

## Identifiers

| Column | Type | Description |
|--------|------|-------------|
| `id` | integer | Unique water point identifier |

## Geographic

| Column | Type | Description |
|--------|------|-------------|
| `longitude` | float | GPS longitude |
| `latitude` | float | GPS latitude |
| `basin` | categorical | Water basin |
| `region` | categorical | Administrative region |
| `region_code` | integer | Region code |
| `district_code` | integer | District code |

## Water Point Details

| Column | Type | Description |
|--------|------|-------------|
| `amount_tsh` | float | Total static head (water amount) |
| `date_recorded` | date | Survey date |
| `funder` | categorical | Funding organization |
| `installer` | categorical | Installation organization |
| `wpt_name` | text | Water point name |
| `construction_year` | integer | Year constructed |
| `waterpoint_type` | categorical | Type of water point |
| `extraction_type` | categorical | Extraction method |

## Operational

| Column | Type | Description |
|--------|------|-------------|
| `management` | categorical | Management group |
| `management_group` | categorical | Management category |
| `payment` | categorical | Payment scheme |
| `water_quality` | categorical | Quality assessment |
| `quantity` | categorical | Quantity assessment |
| `source` | categorical | Water source type |
| `public_meeting` | boolean | Public meeting held |
| `permit` | boolean | Permit status |
| `population` | integer | Population served |

## Target (labels file)

| Column | Type | Description |
|--------|------|-------------|
| `status_group` | categorical | Pump functionality class |

## Notes

- Invalid GPS coordinates `(0, 0)` are treated as missing
- `construction_year == 0` indicates unknown year
- High-cardinality text columns may be dropped or encoded during modeling
