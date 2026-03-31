import pandas as pd
import streamlit as st


def prepare_data(df):
    df_clean = df.copy()

    # Remplacer les valeurs manquantes
    for col in df_clean.columns:
        if df_clean[col].dtype in ['float64', 'int64']:
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
        else:
            df_clean[col].fillna("Inconnu", inplace=True)

    # Standardiser les types
    for col in df_clean.select_dtypes(include=['object']):
        df_clean[col] = df_clean[col].astype(str)

    # Colonnes dérivées
    if 'Revenu' in df_clean.columns:
        df_clean['Revenu_>60k'] = df_clean['Revenu'] > 60000
    if 'Age' in df_clean.columns:
        df_clean['Jeune_<30'] = df_clean['Age'] < 30

    st.success("Données préparées pour l'analyse !")
    return df_clean