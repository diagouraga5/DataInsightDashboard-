import streamlit as st


def filter_data(df):
    df_filtered = df.copy()
    st.sidebar.subheader("Filtres avancés")

    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            min_val = float(df[col].min())
            max_val = float(df[col].max())
            selected_range = st.sidebar.slider(f"{col} :", min_val, max_val, (min_val, max_val))
            df_filtered = df_filtered[(df_filtered[col] >= selected_range[0]) & (df_filtered[col] <= selected_range[1])]
        else:
            options = df[col].unique().tolist()
            selected = st.sidebar.multiselect(f"{col} :", options, default=options)
            df_filtered = df_filtered[df_filtered[col].isin(selected)]

    st.sidebar.write(f"Lignes après filtrage : {len(df_filtered)}")
    return df_filtered