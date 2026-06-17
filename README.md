# Tanzania Water Pump Status Prediction — EDA, Feature Engineering & Multi-Class ML

> **AquaPredict** · End-to-end machine learning pipeline on 59K+ Tanzania water points: data cleaning, exploratory analysis, multi-class classification (functional / needs repair / non-functional), and model evaluation using DrivenData Pump It Up data.

## Impact

Millions of people in Tanzania depend on water pumps for clean drinking water. Predicting which pumps are functional, need repair, or are non-functional helps prioritize maintenance and improve rural water access. This project builds a full classification pipeline on real open data.

## About the Data

Dataset: **DrivenData [Pump It Up](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/)** — Taarifa open data on Tanzania water points (~59,000 training records).

**Target:** 3-class classification
- `functional`
- `functional needs repair`
- `non functional`

## Key Results

- End-to-end pipeline: data cleaning → EDA → feature engineering → classification
- Exploratory analysis of geographic, operational, and construction features
- Multi-class model with evaluation metrics

## Tech Stack

Python · pandas · scikit-learn · Jupyter · matplotlib · seaborn

## Documentation

| Doc | Description |
|-----|-------------|
| [Problem Statement](docs/01-problem-statement.md) | Context and objectives |
| [Data Dictionary](docs/02-data-dictionary.md) | Key features and columns |
| [Modeling Approach](docs/03-modeling-approach.md) | Pipeline overview |
| [Final Report](reports/classification_report.pdf) | Complete analysis write-up |

## Project Structure

```
waterpump-failure-imbalanced-classification/
├── notebooks/
│   ├── 01_eda_and_exploration.ipynb
│   └── 02_classification_model.ipynb
├── src/
│   └── clean_water_data.py
├── data/
│   ├── training_values.csv
│   └── training_labels.csv
├── docs/
└── reports/
```

## Setup & Usage

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_eda_and_exploration.ipynb
```

To regenerate cleaned data:

```bash
python src/clean_water_data.py
```

## Skills Demonstrated

- Exploratory data analysis on real-world humanitarian data
- Feature engineering and data cleaning
- Multi-class classification
- Model evaluation and interpretation

## License

MIT
