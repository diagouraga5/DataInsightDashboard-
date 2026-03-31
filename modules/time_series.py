import plotly.graph_objects as go
import pandas as pd
import numpy as np

def plot_time_series(df, date_col, value_col):

    df = df.copy()

    # Conversion date
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

    # Nettoyage
    df = df.dropna(subset=[date_col, value_col])

    # Tri
    df = df.sort_values(by=date_col)

    # Régression
    df["date_num"] = df[date_col].map(pd.Timestamp.toordinal)

    coef = np.polyfit(df["date_num"], df[value_col], 1)
    trend = np.poly1d(coef)

    df["trend"] = trend(df["date_num"])

    # Graphique
    fig = go.Figure()

    # Nuage de points
    fig.add_trace(go.Scatter(
        x=df[date_col],
        y=df[value_col],
        mode='markers',
        name='Données'
    ))

    # Droite de régression
    fig.add_trace(go.Scatter(
        x=df[date_col],
        y=df["trend"],
        mode='lines',
        name='Régression',
        line=dict(width=3)
    ))

    fig.update_layout(
        title="Série temporelle avec tendance",
        xaxis_title="Date",
        yaxis_title=value_col,
        template="plotly_white"
    )

    return fig