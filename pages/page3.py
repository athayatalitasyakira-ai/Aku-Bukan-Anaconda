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

st.write("Berdasarkan data pergerakan indeks saham dari januari hingga Desember 2025, ketiga indeks—Composite Index, LQ45, dan IDX30—menunjukkan tren kenaikan secara umum, meskipun disertai volatilitas yang signifikan. Composite Index naik dari sekitar 7.163 menjadi 8.650, sementara LQ45 dan IDX30 juga mengalami peningkatan serupa. Pasar sempat mengalami koreksi tajam pada Februari–Maret 2025, dengan Composite Index mencapai titik terendah di 6.161, namun berhasil pulih dan bahkan mencatat level tertinggi baru menjelang akhir periode. Saham blue-chip dalam LQ45 dan IDX30 tampak lebih stabil dibandingkan indeks luas, mencerminkan ketahanan yang lebih baik selama fase fluktuasi.")
    
import streamlit as st
import pandas as pd
import os

st.title("🏆 Ranking Saham Berdasarkan Pertumbuhan")

# Path file Excel
BASE_DIR = os.getcwd()
FILE_PATH = os.path.join(BASE_DIR, "data", "data_saham_prakbigdata.xlsx")

# Cek file
if not os.path.exists(FILE_PATH):
    st.error("File Excel tidak ditemukan")
    st.stop()

# Baca data
df = pd.read_excel(FILE_PATH, engine="openpyxl")
df.columns = df.columns.str.strip()  # bersihkan spasi

# Pastikan kolom Tanggal datetime
df['Tanggal'] = pd.to_datetime(df['Tanggal'])

# Filter tanggal manual
start_date = pd.to_datetime("2025-01-02")
end_date = pd.to_datetime("2025-12-15")
filtered_df = df[(df['Tanggal'] >= start_date) & (df['Tanggal'] <= end_date)]

# ==============================
# Ranking pertumbuhan saham
# ==============================
# Ambil semua kolom harga saham (kolom 1 ke seterusnya, asumsi kolom pertama Tanggal)
price_columns = filtered_df.columns[1:]

# Hitung return: (harga terakhir / harga pertama) - 1
returns = filtered_df.iloc[-1][price_columns] / filtered_df.iloc[0][price_columns] - 1

st.subheader(f"Ranking Saham dari {start_date.date()} sampai {end_date.date()}")
st.dataframe(returns.sort_values(ascending=False))

st.write("Dalam periode 2 Januari hingga 15 Desember 2025, Composite Index menunjukkan pertumbuhan paling kuat sebesar 20,75%, sementara indeks blue-chip seperti IDX30 dan LQ45 hanya tumbuh masing-masing 2,51% dan 1,87%. Hal ini mengindikasikan bahwa penggerak pasar saham terutama berasal dari saham di luar kategori blue-chip.")