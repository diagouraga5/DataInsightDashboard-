import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def show_overview(df):
    """Affiche histogrammes et scatterplots simples"""
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    st.subheader("Histogrammes des variables numériques")
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f"Distribution de {col}")
        st.pyplot(fig)

    if len(numeric_cols) >= 2:
        st.subheader("Scatterplots entre variables numériques")
        for i in range(len(numeric_cols) - 1):
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[numeric_cols[i]], y=df[numeric_cols[i + 1]], ax=ax)
            ax.set_title(f"{numeric_cols[i]} vs {numeric_cols[i + 1]}")
            st.pyplot(fig)