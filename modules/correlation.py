import streamlit as st
import plotly.express as px

def correlation_heatmap(df):
    numeric_cols = df.select_dtypes(include=['float64','int64']).columns
    corr = df[numeric_cols].corr()
    fig = px.imshow(corr, text_auto=True, color_continuous_scale='Viridis', title="Matrice de corrélation")
    st.plotly_chart(fig)