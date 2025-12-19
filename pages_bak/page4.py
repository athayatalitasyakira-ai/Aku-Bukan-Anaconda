import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.set_page_config(page_title="Data Saham", layout="wide")

# Fungsi konversi tanggal Excel
def excel_serial_to_date(x):
    if isinstance(x, (int, float)):
        return datetime(1899, 12, 30) + timedelta(days=x)
    try:
        return pd.to_datetime(x)
    except Exception:
        return pd.NaT

st.title("📈 Visualisasi Data Harga Saham")

# Load data
df = pd.read_excel("Data Harga Saham Prakbigdata.xlsx")

df["Tanggal"] = df["Tanggal"].apply(excel_serial_to_date)
df = df.dropna(subset=["Tanggal"])
df = df.sort_values("Tanggal")

# Pilih saham
saham = st.selectbox(
    "Pilih Indeks Saham",
    ["Composite_Index", "LQ45", "IDX30"]
)

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Tanggal"], df[saham])
ax.set_title(f"Pergerakan {saham}")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Harga")
ax.grid(True)

st.pyplot(fig)

# Statistik
st.subheader("📊 Ringkasan Statistik")
st.write(f"Periode data : {df['Tanggal'].min().date()} s.d {df['Tanggal'].max().date()}")
st.write(f"Harga terendah : {df[saham].min():.2f}")
st.write(f"Harga tertinggi : {df[saham].max():.2f}")
st.write(f"Rata-rata : {df[saham].mean():.2f}")
