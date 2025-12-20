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
    
import pandas as pd
import streamlit as st

# Pastikan kolom Tanggal tipe datetime
df['Tanggal'] = pd.to_datetime(df['Tanggal'])

# Tentukan range tanggal secara manual
start_date = pd.to_datetime("2025-01-02")
end_date = pd.to_datetime("2025-12-15")

# Filter data sesuai tanggal
filtered_df = df[(df['Tanggal'] >= start_date) & (df['Tanggal'] <= end_date)]

# Tampilkan hasil filter
st.subheader(f"Data Saham dari {start_date.date()} sampai {end_date.date()}")
st.dataframe(filtered_df)


