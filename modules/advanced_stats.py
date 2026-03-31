from scipy import stats
import pandas as pd

def t_test(df, col1, col2):
    return stats.ttest_ind(df[col1].dropna(), df[col2].dropna())

def chi2_test(df, col1, col2):
    contingency = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    return chi2, p, dof