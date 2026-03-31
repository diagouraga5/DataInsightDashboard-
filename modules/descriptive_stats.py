import pandas as pd


def descriptive_statistics(df):
    """
    Calcule les statistiques descriptives des colonnes numériques.
    Retourne un DataFrame avec mean, median, std, min, max.
    """
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if numeric_cols.empty:
        return pd.DataFrame()  # rien à calculer

    stats = df[numeric_cols].describe().T  # mean, std, min, 25%, 50%, 75%, max
    stats = stats.rename(columns={"50%": "median"})
    return stats[['mean', 'median', 'std', 'min', 'max']]