import pandas as pd

def chatbot_response(question, df):

    question = question.lower()

    # Nombre de lignes
    if "ligne" in question or "rows" in question:
        return f"Le dataset contient {df.shape[0]} lignes."

    # Colonnes
    elif "colonne" in question:
        return f"Les colonnes sont : {', '.join(df.columns)}"

    # Moyenne
    elif "moyenne" in question:
        num_cols = df.select_dtypes(include=['int64','float64']).columns
        result = []
        for col in num_cols:
            result.append(f"{col} : {df[col].mean():.2f}")
        return "\n".join(result)

    # Maximum
    elif "maximum" in question or "max" in question:
        num_cols = df.select_dtypes(include=['int64','float64']).columns
        result = []
        for col in num_cols:
            result.append(f"{col} : {df[col].max():.2f}")
        return "\n".join(result)

    # Corrélation
    elif "corrélation" in question:
        corr = df.corr(numeric_only=True)
        return corr.to_string()

    # Anomalies simples
    elif "anomalie" in question:
        num_cols = df.select_dtypes(include=['int64','float64']).columns
        anomalies = []
        for col in num_cols:
            if df[col].max() > df[col].mean() * 3:
                anomalies.append(col)
        return f"Colonnes avec anomalies : {', '.join(anomalies)}"

    else:
        return "Je n’ai pas encore compris cette question. Essaie avec : moyenne, max, corrélation, anomalies..."