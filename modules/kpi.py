import pandas as pd

def calculate_kpis(df):
    kpis = {}
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
    if numeric_cols:
        for col in numeric_cols:
            kpis[f"{col}_mean"] = df[col].mean()
            kpis[f"{col}_median"] = df[col].median()
            kpis[f"{col}_max"] = df[col].max()
            kpis[f"{col}_min"] = df[col].min()
    kpis['rows'] = len(df)
    kpis['columns'] = df.shape[1]
    return kpis