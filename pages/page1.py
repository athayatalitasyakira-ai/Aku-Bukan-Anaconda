import streamlit as st

st.title("Welcome to Aku Bukan Anaconda's Homepage")
st.write("Tugas Akhir Praktikum Big Data")

# Anggota kelompok
st.subheader("👥 Nama Anggota Kelompok")
st.write("1. Athaya Talita Syakira (021002301012)")
st.write("2. Wafiq Azizah (021002305001)")
st.write("3. Chyntia Indra Lokananta Joe Aleya (021002301002)")
st.write("4. Lintang Puji Lestari (021002302001)")

# Tujuan pengambilan data
st.subheader("🎯 Tujuan Pengambilan Data Saham")
st.write(
    "Pengambilan data dari tiga saham dalam proyek tugas Praktikum Big Data bertujuan untuk menganalisis dan membandingkan pergerakan harga serta kinerja saham secara komparatif. "
    "Data tersebut digunakan untuk menerapkan proses pengolahan Big Data, mulai dari pengumpulan, pembersihan, hingga analisis dan visualisasi data, "
    "sehingga mahasiswa dapat memahami pola, tren, dan karakteristik masing-masing saham. "
    "Selain itu, proyek ini bertujuan meningkatkan kemampuan pengambilan keputusan berbasis data melalui analisis data saham secara sistematis dan objektif."
)

st.write("Data diambil dari daily IDX indices")

# -----------------------------
# Preview Data Saham
# -----------------------------
import pandas as pd
import os

st.subheader("📋 Preview Data Saham")

# Lokasi file (folder: data/)
BASE_DIR = os.getcwd()
FILE_PATH = os.path.join(BASE_DIR, "data", "data_saham_prakbigdata.xlsx")

# Cek apakah file ada
if not os.path.exists(FILE_PATH):
    st.warning("⚠ File Excel belum ditemukan di folder **data/**")
    st.info("Silakan pastikan file ada di: data/data_saham_prakbigdata.xlsx")
else:
    df = pd.read_excel(FILE_PATH, engine="openpyxl")
    st.dataframe(df.head())





