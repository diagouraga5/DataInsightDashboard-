import streamlit as st
from sklearn.ensemble import RandomForestRegressor
import pandas as pd


def feature_importance(df, target, features):
    X = df[features]
    y = df[target]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    importance = pd.DataFrame({'Feature': features, 'Importance': model.feature_importances_}).sort_values(
        by='Importance', ascending=False)
    st.subheader("Importance des variables")
    st.bar_chart(importance.set_index('Feature'))