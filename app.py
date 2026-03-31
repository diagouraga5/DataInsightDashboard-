import streamlit as st
import pandas as pd

# Modules
from modules.data_loader import load_data
from modules.data_prep import prepare_data
from modules.modern_kpi import calculate_modern_kpis
from modules.plotly_viz import plotly_hist, plotly_scatter
from modules.regression import linear_regression
from modules.advanced_stats import chi2_test
from modules.descriptive_stats import descriptive_statistics
from modules.time_series import plot_time_series
from modules.correlation import correlation_heatmap
from modules.clustering import kmeans_clustering
from modules.feature_importance import feature_importance
from modules.geo_viz import plot_geo
from modules.alerts_advanced import alert_anomalies
from modules.report import create_pdf_report
from modules.ai_insights import generate_insights
from modules.chatbot import chatbot_response
from modules.chatbot_advanced import chatbot_advanced

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="Wagadou Dashboard", layout="wide")

# -----------------------------
# STYLE
# -----------------------------
st.markdown("""
<style>
.kpi-card {
    background: linear-gradient(135deg, #6A0DAD, #1E90FF);
    padding: 15px;
    border-radius: 10px;
    color: white;
    text-align: center;
}
.footer {
    background-color:#f2f2f2;
    padding:10px;
    border-radius:10px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<h1 style='color:#6A0DAD;'>🌟 Wagadou Academy Dashboard</h1>
<p>Analyse intelligente • Visualisation • IA intégrée</p>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.image("logo_wagadou.png", width=120)

    menu = st.radio("Navigation", [
        "🏠 Accueil",
        "📊 KPIs",
        "📈 Visualisations",
        "📉 Statistiques descriptives",
        "🧠 Modèles",
        "📊 Corrélation",
        "⏳ Séries temporelles",
        "🤖 Machine Learning",
        "🌍 Géovisualisation",
        "⚠️ Alertes",
        "🤖 IA Insights",
        "💬 Chatbot IA",
        "💬 Chatbot IA Avancé",
        "📄 Rapport"
    ])

# -----------------------------
# IMPORT DATA
# -----------------------------
file = st.file_uploader("📥 Importer CSV / Excel", type=["csv","xlsx","xls"])

if file:
    df = prepare_data(load_data(file))
else:
    df = None

# -----------------------------
# ACCUEIL
# -----------------------------
if menu == "🏠 Accueil":
    st.subheader("Aperçu des données")
    if df is not None:
        st.dataframe(df.head())
    else:
        st.info("Importer un fichier pour commencer")

# -----------------------------
# KPIs
# -----------------------------
elif menu == "📊 KPIs":
    if df is not None:
        kpis = calculate_modern_kpis(df)
        cols = st.columns(len(kpis))
        for i, (k, v) in enumerate(kpis.items()):
            cols[i].markdown(f"<div class='kpi-card'><h4>{k}</h4><h2>{v}</h2></div>", unsafe_allow_html=True)
    else:
        st.warning("Importer un fichier")

# -----------------------------
# VISUALISATIONS
# -----------------------------
elif menu == "📈 Visualisations":
    if df is not None:
        plotly_hist(df)
        plotly_scatter(df)
    else:
        st.warning("Importer un fichier")

# -----------------------------
# STATISTIQUES DESCRIPTIVES
# -----------------------------
elif menu == "📉 Statistiques descriptives":
    if df is not None:
        st.subheader("Statistiques descriptives")
        st.dataframe(descriptive_statistics(df))
    else:
        st.warning("Importer un fichier")

# -----------------------------
# MODELES
# -----------------------------
elif menu == "🧠 Modèles":
    if df is not None:
        numeric_cols = df.select_dtypes(include=['int64','float64']).columns

        if len(numeric_cols) >= 2:
            target = st.selectbox("Cible", numeric_cols)
            features = st.multiselect("Variables explicatives", [c for c in numeric_cols if c != target])

            if features:
                model, summary = linear_regression(df, target, features)
                st.text(summary)

        cat_cols = df.select_dtypes(include=['object']).columns
        if len(cat_cols) >= 2:
            c1 = st.selectbox("Catégorie 1", cat_cols)
            c2 = st.selectbox("Catégorie 2", [c for c in cat_cols if c != c1])
            chi2, p, dof = chi2_test(df, c1, c2)
            st.write(f"Chi2={chi2:.2f}, p={p:.4f}")
    else:
        st.warning("Importer un fichier")

# -----------------------------
# CORRELATION
# -----------------------------
elif menu == "📊 Corrélation":
    if df is not None:
        correlation_heatmap(df)
    else:
        st.warning("Importer un fichier")

# -----------------------------
# SERIES TEMPORELLES
# -----------------------------
# -----------------------------
# SERIES TEMPORELLES
# -----------------------------

elif menu == "⏳ Séries temporelles":

    if df is not None:

        st.subheader("📈 Analyse temporelle")

        # Choix des colonnes
        date_col = st.selectbox("Choisir la colonne date", df.columns)

        numeric_cols = df.select_dtypes(include=['int64','float64']).columns

        if len(numeric_cols) == 0:
            st.error("Aucune colonne numérique disponible")
            st.stop()

        value_col = st.selectbox("Choisir la variable", numeric_cols)

        if st.button("Afficher le graphique"):

            try:
                fig = plot_time_series(df, date_col, value_col)
                st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.error(f"Erreur : {e}")

    else:
        st.warning("Importer un fichier")
# -----------------------------
# GEO
# -----------------------------
elif menu == "🌍 Géovisualisation":
    if df is not None:
        cols = df.select_dtypes(include=['float64','int64']).columns
        if len(cols) >= 2:
            lat = st.selectbox("Latitude", cols)
            lon = st.selectbox("Longitude", [c for c in cols if c != lat])
            plot_geo(df, lat, lon)
    else:
        st.warning("Importer un fichier")

# -----------------------------
# ALERTES
# -----------------------------
elif menu == "⚠️ Alertes":
    if df is not None:
        col = st.selectbox("Colonne", df.select_dtypes(include=['int64','float64']).columns)
        seuil = st.slider("Seuil", 1.0, 5.0, 3.0)
        alert_anomalies(df, col, "zscore", seuil)
    else:
        st.warning("Importer un fichier")

# -----------------------------
# IA INSIGHTS
# -----------------------------
elif menu == "🤖 IA Insights":
    if df is not None:
        insights = generate_insights(df)
        for insight in insights:
            st.write(insight)
    else:
        st.warning("Importer un fichier")

# -----------------------------
# CHATBOT SIMPLE
# -----------------------------
elif menu == "💬 Chatbot IA":
    if df is not None:
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        user_input = st.text_input("Pose ta question")

        if st.button("Envoyer"):
            response = chatbot_response(user_input, df)
            st.session_state.chat_history.append(("Vous", user_input))
            st.session_state.chat_history.append(("IA", response))

        for sender, msg in st.session_state.chat_history:
            st.write(f"{sender}: {msg}")
    else:
        st.warning("Importer un fichier")

# -----------------------------
# CHATBOT AVANCE
# -----------------------------
elif menu == "💬 Chatbot IA Avancé":
    if df is not None:
        user_input = st.text_input("Question avancée")

        if st.button("Analyser"):
            response = chatbot_advanced(user_input, df)
            st.write(response)
    else:
        st.warning("Importer un fichier")

# -----------------------------
# RAPPORT
# -----------------------------
elif menu == "📄 Rapport":
    if df is not None:
        if st.button("Générer PDF"):
            create_pdf_report(df)
    else:
        st.warning("Importer un fichier")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("👤 Salim Diagouraga | Wagadou Academy")