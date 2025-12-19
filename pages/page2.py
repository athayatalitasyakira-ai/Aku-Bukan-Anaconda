import streamlit as st
import pandas as pd
import os

st.title("📊 Data Saham")


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


FILE_PATH = os.path.join(BASE_DIR, "data", "data_saham_")


if not os.path.exists(FILE_PATH):
    st.error("❌ File data_saham.xlsx tidak ditemukan di folder data")
    st.stop()


df = pd.read_excel('data_saham_')

st.success("✅ Data berhasil dimuat")


st.write("Kolom tersedia:", df.columns.tolist())


if "Perusahaan" not in df.columns:
    st.error("❌ Kolom 'Perusahaan' tidak ditemukan di file Excel")
    st.stop()


perusahaan = st.selectbox(
    "Pilih Perusahaan",
    df["Perusahaan"].unique()
)


data_perusahaan = df[df["Perusahaan"] == perusahaan]

st.subheader("📈 Detail Data")
st.dataframe(data_perusahaan)
