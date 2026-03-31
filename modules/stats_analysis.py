import pandas as pd
from scipy import stats

def descriptive_stats(df):
    """Retourne un résumé statistique complet"""
    desc = df.describe(include='all').T
    desc['missing_values'] = df.isnull().sum()
    desc['unique_values'] = df.nunique()
    return desc

def correlation_matrix(df):
    """Retourne la matrice de corrélation pour variables numériques"""
    return df.corr()

def t_test(df, col1, col2):
    """Effectue un t-test entre deux colonnes numériques"""
    return stats.ttest_ind(df[col1].dropna(), df[col2].dropna())

def chi2_test(df, col1, col2):
    """Effectue un test Chi² entre deux colonnes catégorielles"""
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
    return chi2, p, dof, expected