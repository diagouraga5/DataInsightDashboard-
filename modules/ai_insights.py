import pandas as pd

def generate_insights(df):
    insights = []

    # 1. Analyse générale
    insights.append(f"Le dataset contient {df.shape[0]} lignes et {df.shape[1]} colonnes.")

    # 2. Analyse des variables numériques
    num_cols = df.select_dtypes(include=['int64','float64']).columns

    for col in num_cols:
        mean = df[col].mean()
        max_val = df[col].max()
        min_val = df[col].min()

        insights.append(f"La variable {col} a une moyenne de {mean:.2f}, "
                        f"un minimum de {min_val:.2f} et un maximum de {max_val:.2f}.")

        # Détection simple anomalies
        if max_val > mean * 3:
            insights.append(f"⚠️ La variable {col} présente des valeurs extrêmes.")

    # 3. Corrélation
    if len(num_cols) >= 2:
        corr = df[num_cols].corr().abs()
        high_corr = (corr > 0.7) & (corr < 1)

        for col in corr.columns:
            for row in corr.index:
                if high_corr.loc[row, col]:
                    insights.append(f"🔗 Forte corrélation entre {row} et {col}")

    return insights