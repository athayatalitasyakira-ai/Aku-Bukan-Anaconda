import os
import streamlit as st
import pandas as pd

st.title("📈 Analisis Data Saham")


BASE_DIR = os.path.dirname(os.path.dirname(data_saham_baru))
FILE_PATH = os.path.join(BASE_DIR, "data", "data_saham_baru")


if not os.path.exists(FILE_PATH):
    st.error("File data_saham.xlsx tidak ditemukan di folder data")
    st.stop()


df = pd.read_excel(FILE_PATH)


df.columns = df.columns.str.strip()

st.subheader("📋 Preview Data")
st.dataframe(df)

st.subheader("🔍 Daftar Kolom")
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
