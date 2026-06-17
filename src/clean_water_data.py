"""
Load, merge, and clean the Pump It Up (Tanzania waterpoints) training CSVs.
Run: python clean_water_data.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

# Step 1: Paths to the two CSV files (project data/ directory).
HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
VALUES_CSV = DATA_DIR / "training_values.csv"
LABELS_CSV = DATA_DIR / "training_labels.csv"

# Step 2: Import the feature table — one row per waterpoint (survey fields).
values_df = pd.read_csv(VALUES_CSV, low_memory=False)

# Step 3: Import the label table — id + pump status (classification target).
labels_df = pd.read_csv(LABELS_CSV, low_memory=False)

# Step 4a: If duplicate ids exist, keep the first row so the merge is one row per id.
values_df = values_df.drop_duplicates(subset=["id"], keep="first")
labels_df = labels_df.drop_duplicates(subset=["id"], keep="first")

# Step 4b: Join on id so each row has both features and status_group (inner = ids in both files).
df = values_df.merge(labels_df, on="id", how="inner")

# Step 5: Drop duplicate ids if any slipped through.
df = df.drop_duplicates(subset=["id"], keep="first")

# Step 6: For object/string columns, turn empty strings into missing (NaN).
obj_cols = [
    c
    for c in df.columns
    if pd.api.types.is_object_dtype(df[c]) or pd.api.types.is_string_dtype(df[c])
]
for col in obj_cols:
    df[col] = df[col].replace(r"^\s*$", np.nan, regex=True)

# Step 7: Strip leading/trailing whitespace on text fields.
for col in obj_cols:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

# Step 8: Parse date_recorded as datetime (for later features like pump age).
df["date_recorded"] = pd.to_datetime(df["date_recorded"], errors="coerce")

# Step 9: Keep only rows recorded in 2011, 2012, or 2013 as requested.
df = df[df["date_recorded"].dt.year.isin([2011, 2012, 2013])]

# Step 10: Invalid GPS (0, 0) is not in Tanzania — set to NaN.
bad_geo = (df["longitude"] == 0) & (df["latitude"] == 0)
df.loc[bad_geo, ["longitude", "latitude"]] = np.nan

# Step 11: construction_year == 0 means unknown — replace with NaN.
df.loc[df["construction_year"] == 0, "construction_year"] = np.nan

# Step 12: Negative population is invalid.
df.loc[df["population"] < 0, "population"] = np.nan

# Step 13: Negative amount_tsh is invalid (0 is valid “no fee”).
df.loc[df["amount_tsh"] < 0, "amount_tsh"] = np.nan

# Step 14: Standardize boolean-like columns (CSV mixes bool, strings, blanks).
for col in ("public_meeting", "permit"):
    df[col] = df[col].map(
        {
            True: True,
            False: False,
            "True": True,
            "False": False,
            "true": True,
            "false": False,
        }
    )

# Step 15: Drop rows with no label.
df = df.dropna(subset=["status_group"])

# Step 16: Linear regression needs numeric/categorical inputs — not raw datetimes.
# Keep a numeric year from date_recorded, then drop the datetime column.
df["record_year"] = df["date_recorded"].dt.year

# Step 17: Drop columns that are not suitable for ordinary linear regression (as-is).
# Keep id for now so you can align rows when training/testing on the same file (drop id before fitting the model).
# - date_recorded: datetime dtype; replaced by record_year above.
# - recorded_by / num_private: near-constant or no useful signal in this dataset.
# - wpt_name, subvillage, scheme_name, funder, installer: very high cardinality text → huge/unstable one-hot.
# - ward, lga: very many levels; region/basin/region_code already summarize geography.
# - Duplicate “group” columns (same information as the main column, multicollinearity if both one-hot encoded).
cols_to_drop = [
    "date_recorded",
    "recorded_by",
    "num_private",
    "wpt_name",
    "subvillage",
    "scheme_name",
    "funder",
    "installer",
    "ward",
    "lga",
    "extraction_type_group",
    "extraction_type_class",
    "payment_type",
    "quality_group",
    "quantity_group",
    "source_type",
    "source_class",
    "waterpoint_type_group",
    "management_group",
]
df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

# Step 18: One-hot encode the target (status_group) for multi-output linear regression.
# Each row gets a 1 in exactly one column: 0/1 indicators for each class.
target_onehot = pd.get_dummies(df["status_group"], prefix="target").astype(int)
target_onehot.columns = [c.replace(" ", "_") for c in target_onehot.columns]
df = pd.concat([df.drop(columns=["status_group"]), target_onehot], axis=1)

# Step 19: Save cleaned table for notebooks / modeling.
out_path = DATA_DIR / "pump_train_cleaned.csv"
df.to_csv(out_path, index=False)

print(f"Rows (values): {len(values_df):,}")
print(f"Rows (labels): {len(labels_df):,}")
print(f"Rows after merge & clean: {len(df):,}")
print(f"Columns in output ({len(df.columns)}): {', '.join(df.columns)}")
print(f"Saved: {out_path}")
