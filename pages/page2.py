import streamlit as st
import pandas as pd

st.title("📈 Analisis Data Saham")

uploaded_file = st.file_uploader(
    "Upload file Excel data saham",
    type=["xlsx"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    df.columns = df.columns.str.strip()

    st.subheader("📋 Preview Data")
    st.dataframe(df)

    st.subheader("🔍 Nama Kolom")
    st.write(df.columns.tolist())

    kolom_perusahaan = st.selectbox(
        "Pilih kolom nama perusahaan:",
        df.columns
    )

    perusahaan = st.selectbox(
        "Pilih perusahaan:",
        df[kolom_perusahaan].dropna().unique()
    )

    data_perusahaan = df[df[kolom_perusahaan] == perusahaan]

    st.subheader(f"📌 Data untuk {perusahaan}")
    st.dataframe(data_perusahaan)

else:
    st.info("⬆️ Silakan upload file Excel terlebih dahulu")
