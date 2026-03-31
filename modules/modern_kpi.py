import streamlit as st


def calculate_modern_kpis(df):
    kpis = {}
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()

    kpis['Total_rows'] = len(df)
    kpis['Total_columns'] = df.shape[1]

    if 'Revenu' in numeric_cols:
        kpis['Moyenne_Revenu'] = df['Revenu'].mean()
        kpis['Median_Revenu'] = df['Revenu'].median()
        kpis['Revenu>60k'] = (df['Revenu'] > 60000).sum()

    if 'Score_achat' in numeric_cols:
        kpis['Max_Score'] = df['Score_achat'].max()
        kpis['Min_Score'] = df['Score_achat'].min()

    if 'Age' in numeric_cols:
        kpis['Age<30'] = (df['Age'] < 30).sum()

    if 'Sexe' in cat_cols:
        sexe_count = df['Sexe'].value_counts(normalize=True) * 100
        for s in sexe_count.index:
            kpis[f"%{s}"] = round(sexe_count[s], 1)

    if 'Region' in cat_cols and 'Score_achat' in numeric_cols:
        region_score = df.groupby('Region')['Score_achat'].mean()
        kpis['Region_top_score'] = region_score.idxmax()

    return kpis


def display_modern_kpis(kpis):
    st.subheader("Indicateurs clés")
    cols = st.columns(len(kpis))
    for i, (key, value) in enumerate(kpis.items()):
        value_display = f"{value:.2f}" if isinstance(value, float) else str(value)
        cols[i].metric(label=key, value=value_display)