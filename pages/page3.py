import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Perbandingan Saham", layout="wide")
st.title("📊 Perbandingan Saham")

# -----------------------------
# Path file Excel
# -----------------------------
BASE_DIR = os.getcwd()
FILE_PATH = os.path.join(BASE_DIR, "data", "data_saham_prakbigdata.xlsx")

if not os.path.exists(FILE_PATH):
    st.error("❌ File Excel tidak ditemukan di folder 'data'")
    st.stop()

# -----------------------------
# Baca data
# -----------------------------
df = pd.read_excel(FILE_PATH, engine="openpyxl")
df.columns = df.columns.str.strip()  # bersihkan spasi di kolom

st.subheader("📌 Tabel Data Saham")
st.dataframe(df)  # tampil seluruh data

# -----------------------------
# Pilih kolom numeric (harga saham)
# -----------------------------
numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
if not numeric_cols:
    st.error("❌ Tidak ada kolom numeric untuk diplot")
    st.stop()

# -----------------------------
# Multiselect interaktif untuk memilih saham
# -----------------------------
selected_stocks = st.multiselect(
    "Pilih saham yang ingin dibandingkan:",
    options=numeric_cols,
    default=numeric_cols  # default semua kolom
)

if selected_stocks:
    st.subheader("📈 Grafik Perbandingan Saham")
    fig, ax = plt.subplots(figsize=(12,6))
    df[selected_stocks].plot(ax=ax)
    ax.set_xlabel("Index / Waktu")
    ax.set_ylabel("Harga Saham")
    ax.set_title("Perbandingan Saham Terpilih")
    ax.legend(selected_stocks)
    st.pyplot(fig)
    
df['Tanggal'] = pd.to_datetime(df['Tanggal'])  # pastikan ada kolom tanggal
start_date = st.date_input("Mulai dari", df['Tanggal'].min())
end_date = st.date_input("Sampai", df['Tanggal'].max())

filtered_df = df[(df['Tanggal'] >= start_date) & (df['Tanggal'] <= end_date)]

