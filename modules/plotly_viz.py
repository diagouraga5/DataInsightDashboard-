import streamlit as st
import plotly.express as px

def plotly_hist(df):
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    for col in numeric_cols:
        fig = px.histogram(df, x=col, marginal="box", color=cat_cols[0] if cat_cols else None)
        st.plotly_chart(fig)

def plotly_scatter(df):
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    if len(numeric_cols) >= 2:
        fig = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1],
                         color=cat_cols[0] if cat_cols else None,
                         size=numeric_cols[0], hover_data=numeric_cols)
        st.plotly_chart(fig)