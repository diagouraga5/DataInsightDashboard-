import streamlit as st

def alert_anomalies(df, column, method="zscore", threshold=3):
    if method=="zscore":
        import numpy as np
        z = (df[column] - df[column].mean()) / df[column].std()
        anomalies = df[z.abs() > threshold]
        if not anomalies.empty:
            st.warning(f"Anomalies détectées dans {column} : {len(anomalies)} lignes")