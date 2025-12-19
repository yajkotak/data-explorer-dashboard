# app/data_manager.py
"""
Load & validate datasets (CSV / XLSX / Parquet) and provide column discovery.
"""

from pathlib import Path
import pandas as pd

SUPPORTED = [".csv", ".xlsx", ".parquet"]

def load_dataset(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"{path} not found")
    suffix = path.suffix.lower()
    if suffix == ".csv":
        df = pd.read_csv(path)
    elif suffix in (".xls", ".xlsx"):
        df = pd.read_excel(path)
    elif suffix == ".parquet":
        df = pd.read_parquet(path)
    else:
        raise ValueError("Unsupported file type. Supported: CSV, XLSX, Parquet")
    return df

def validate_dataset(df, min_rows=10, min_numeric=2):
    """
    Returns (valid:bool, info:dict) where info contains reasons or metadata.
    """
    info = {}
    if df is None:
        return False, {"reason": "No dataframe provided"}
    if df.shape[0] < min_rows:
        return False, {"reason": f"Dataset has {df.shape[0]} rows (< {min_rows})"}
    if df.columns.duplicated().any():
        return False, {"reason": "Duplicate column names found"}
    numeric = df.select_dtypes(include="number").columns.tolist()
    info["n_rows"] = df.shape[0]
    info["n_cols"] = df.shape[1]
    info["numeric_columns"] = numeric
    info["categorical_columns"] = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    if len(numeric) < min_numeric:
        return False, {"reason": f"Need at least {min_numeric} numeric columns (found {len(numeric)})", **info}
    return True, info
