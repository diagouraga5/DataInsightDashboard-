import streamlit as st
import plotly.express as px

def plot_geo(df, lat_col, lon_col, value_col=None):
    fig = px.scatter_mapbox(df, lat=lat_col, lon=lon_col, color=value_col,
                            size=value_col, zoom=4, mapbox_style="carto-positron")
    st.plotly_chart(fig)