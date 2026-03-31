# modules/regression.py

from sklearn.linear_model import LinearRegression
import pandas as pd

def linear_regression(df, target, features):
    X = df[features]
    y = df[target]

    model = LinearRegression()
    model.fit(X, y)

    # Résumé simple
    coef = model.coef_
    intercept = model.intercept_

    summary = f"Intercept: {intercept}\n"
    for f, c in zip(features, coef):
        summary += f"{f}: {c}\n"

    return model, summary