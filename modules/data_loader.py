import pandas as pd
import streamlit as st

def load_data(file):
    """
    Charge un fichier CSV ou Excel et retourne un DataFrame.
    """
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            st.error("Format de fichier non supporté. Utiliser CSV ou Excel.")
            return None
        st.success(f"Données chargées : {df.shape[0]} lignes, {df.shape[1]} colonnes")
        return df
    except Exception as e:
        st.error(f"Erreur lors du chargement : {e}")
        return None