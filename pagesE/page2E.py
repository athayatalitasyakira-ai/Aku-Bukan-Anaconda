import streamlit as st
import pandas as pd
import os

st.title("📊 Data Saham")


BASE_DIR = os.path.dirname(os.path.dirname('Data Saham Prakbigdata.csv BARU'))


FILE_PATH = os.path.join(BASE_DIR, 'Data_Saham_Prakbigdata.csv_BARU')


if not os.path.exists(FILE_PATH):
    st.error("❌ File data_saham.xlsx tidak ditemukan di folder data")
    st.stop()


df = pd.read_excel('Data_Saham_Prakbigdata.csv_BARU')

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

import os
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analisis Data Saham", layout="wide")
st.title("📈 Analisis Data Saham")

# -----------------------------
# Tentukan path file Excel
# -----------------------------
BASE_DIR = os.getcwd()  # folder proyek saat ini
DATA_FOLDER = os.path.join(BASE_DIR, "data")
FILE_NAME = "data_saham_baru.xlsx"
FILE_PATH = os.path.join(DATA_FOLDER, FILE_NAME)

# Debug: cek folder dan file
st.write("Folder data:", DATA_FOLDER)
st.write("File path:", FILE_PATH)

# -----------------------------
# Cek apakah file ada
# -----------------------------
if not os.path.exists(FILE_PATH):
    st.error(f"❌ File {FILE_NAME} tidak ditemukan di folder data")
    st.stop()

# -----------------------------
# Baca file Excel
# -----------------------------
try:
    df = pd.read_excel(FILE_PATH, engine="openpyxl")
except Exception as e:
    st.error(f"❌ Gagal membaca file Excel: {e}")
    st.stop()

# Rapikan nama kolom
df.columns = df.columns.str.strip()

# -----------------------------
# Preview data
# -----------------------------
st.subheader("📋 Preview Data")
st.dataframe(df)

# -----------------------------
# Daftar kolom
# -----------------------------
st.subheader("🔍 Daftar Kolom")
st.write(df.columns.tolist())

# -----------------------------
# Pilih kolom perusahaan
# -----------------------------
kolom_perusahaan = st.selectbox(
    "Pilih kolom nama perusahaan:",
    df.columns
)

# Pilih perusahaan
perusahaan = st.selectbox(
    "Pilih perusahaan:",
    df[kolom_perusahaan].dropna().unique()
)

# Filter data perusahaan
data_perusahaan = df[df[kolom_perusahaan] == perusahaan]

st.subheader(f"📌 Data untuk {perusahaan}")
st.dataframe(data_perusahaan)

