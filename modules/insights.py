import streamlit as st
import plotly.express as px

def display_kpis(kpis):
    st.subheader("Résumé KPI")
    cols = st.columns(len(kpis))
    for i, (key, value) in enumerate(kpis.items()):
        value_display = f"{value:.2f}" if isinstance(value,float) else str(value)
        cols[i].metric(label=key, value=value_display)

def alert_on_threshold(df, column, threshold, direction="above"):
    if direction=="above" and df[column].max() > threshold:
        st.warning(f"Alerte : {column} a dépassé {threshold}")
    elif direction=="below" and df[column].min() < threshold:
        st.warning(f"Alerte : {column} est en dessous de {threshold}")

def plot_summary(df, x_col, y_col):
    fig = px.bar(df, x=x_col, y=y_col, color=y_col, title=f"{y_col} par {x_col}")
    st.plotly_chart(fig)