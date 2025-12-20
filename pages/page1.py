import streamlit as st
import pandas as pd
import os

# -----------------------------
# Judul & Informasi Kelompok
# -----------------------------
st.title("🏠 Home - Analisis data saham")
st.header("Aku Bukan Anaconda")
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

# -----------------------------
# Preview Data Saham
# -----------------------------
st.subheader("📋 Preview Data Saham")

# Cek file default di folder data/
BASE_DIR = os.getcwd()
DEFAULT_FILE = os.path.join(BASE_DIR, "data", "data_saham_prakbigdata.xlsx")  # nama file sudah sesuai

# Fungsi untuk membaca file Excel
def load_excel(file_path):
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        st.error(f"❌ Gagal membaca file: {e}")
        return None

# Jika file default ada, baca
if os.path.exists(DEFAULT_FILE):
    df = load_excel(DEFAULT_FILE)
    if df is not None:
        st.success(f"✅ Data berhasil dibaca dari {DEFAULT_FILE}")
        st.dataframe(df)
# Jika file default tidak ada, gunakan uploader
else:
    st.warning("⚠ File Excel tidak ditemukan di folder 'data/'. Silakan upload file Excel.")
    uploaded_file = st.file_uploader("Upload file Excel (.xlsx)", type=["xlsx"])
    if uploaded_file is not None:
        df = load_excel(uploaded_file)
        if df is not None:
            st.success("✅ Data berhasil dibaca dari file yang diupload")
            st.dataframe(df)
    else:
        st.info("Silakan upload file untuk menampilkan data saham.")
