from fpdf import FPDF
import streamlit as st


def create_pdf_report(df, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Rapport Data Insight Dashboard", ln=True, align="C")

    pdf.ln(10)
    pdf.cell(200, 10, txt="Statistiques descriptives :", ln=True)
    desc = df.describe().round(2)
    for idx, row in desc.iterrows():
        pdf.cell(200, 8, txt=f"{idx}: {row.to_dict()}", ln=True)

    pdf.output(filename)
    st.success(f"Rapport généré : {filename}")