import streamlit as st
from sklearn.cluster import KMeans
import plotly.express as px


def kmeans_clustering(df, features, n_clusters=3):
    X = df[features]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(X)
    df['Cluster'] = kmeans.labels_

    fig = px.scatter(df, x=features[0], y=features[1], color='Cluster', hover_data=features, title="Clustering KMeans")
    st.plotly_chart(fig)
    st.write(df.head())