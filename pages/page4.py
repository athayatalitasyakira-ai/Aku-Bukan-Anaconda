import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.set_page_config(page_title="Perbandingan Saham", layout="wide")

def excel_serial_to_date(serial):
    if isinstance(serial, (int, float)):
        base_date = datetime(1899, 12, 30)
        return base_date + timedelta(days=serial)
    else:
        try:
            return pd.to_datetime(serial)
        except:
            return pd.NaT

st.title("Visualisasi Data Harga Saham")

df = pd.read_excel("Data Harga Saham Prakbigdata.xlsx")
df["Tanggal"] = df["Tanggal"].apply(excel_serial_to_date)
df = df.dropna(subset=["Tanggal"])
df = df.sort_values("Tanggal")

saham_options = ["Composite_Index", "LQ45", "IDX30"]
saham = st.selectbox("Pilih Saham", saham_options)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Tanggal"], df[saham], marker="o")
ax.set_title(f"Data Historis Saham: {saham}")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Harga")
ax.grid(True)
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader("Ringkasan Statistik")
st.write(f"Periode data: {df['Tanggal'].min().date()} sampai {df['Tanggal'].max().date()}")
st.write(f"Harga terendah: {df[saham].min():.2f}")
st.write(f"Harga tertinggi: {df[saham].max():.2f}")
st.write(f"Rata-rata harga: {df[saham].mean():.2f}")