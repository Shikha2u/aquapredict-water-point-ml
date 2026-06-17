# Modeling Approach

## Pipeline Overview

```
Raw CSVs → Merge & Clean → EDA → Feature Engineering → Classifier → Evaluation
```

## Step 1: Data Cleaning (`src/clean_water_data.py`)

- Merge `training_values.csv` and `training_labels.csv` on `id`
- Handle missing values, invalid GPS, unknown construction years
- Filter records to 2011–2013 survey years
- Drop high-cardinality or redundant columns
- Output: `data/pump_train_cleaned.csv` (optional)

## Step 2: Exploratory Data Analysis (`notebooks/01_eda_and_exploration.ipynb`)

- Class distribution (target imbalance)
- Geographic distribution of water points
- Feature distributions by pump status
- Correlation and missing-value analysis

## Step 3: Classification Model (`notebooks/02_classification_model.ipynb`)

- Encode categorical features
- Handle class imbalance (if applicable)
- Train multi-class classifier (e.g. Random Forest, Logistic Regression, or ensemble)
- Evaluate with accuracy, confusion matrix, and per-class metrics

## Step 4: Reporting

- Final write-up in `reports/classification_report.pdf`
- Key findings documented in notebook outputs

## Design Decisions

- **Inner merge** on `id` ensures every row has both features and label
- **Geographic features** (region, basin, lat/long) often strong predictors of maintenance patterns
- **Operational features** (management, payment, installer) capture institutional factors affecting pump longevity
