import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("📊 Grafik Semua Saham")

# -----------------------------
# Path file Excel
# -----------------------------
BASE_DIR = os.getcwd()
FILE_PATH = os.path.join(BASE_DIR, "data", "data_saham_prakbigdata.xlsx")

if not os.path.exists(FILE_PATH):
    st.error("❌ File Excel tidak ditemukan di folder data")
    st.stop()

# -----------------------------
# Baca data
# -----------------------------
df = pd.read_excel(FILE_PATH, engine="openpyxl")
df.columns = df.columns.str.strip()  # bersihkan spasi di nama kolom

# -----------------------------
# Pilih kolom harga saham
# -----------------------------
numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
if not numeric_cols:
    st.error("❌ Tidak ada kolom numeric untuk diplot")
    st.stop()

st.subheader("📈 Grafik Semua Saham")

# -----------------------------
# Plot semua kolom numeric
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 6))
df[numeric_cols].plot(ax=ax)  # plot semua kolom numeric
ax.set_xlabel("Baris / Index")
ax.set_ylabel("Harga Saham")
ax.set_title("Pergerakan Semua Saham")
ax.legend(numeric_cols)
st.pyplot(fig)