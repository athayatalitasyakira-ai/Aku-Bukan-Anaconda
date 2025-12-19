import streamlit as st
import pandas as pd
from pathlib import Path

import os
st.write("Current working directory:", os.getcwd())
st.write("File exists:", os.path.exists(file_path))


st.title("📊 Nilai Saham Perusahaan LQ45")

# =========================
# List Perusahaan LQ45
# =========================
lq45 = [
    "AADI","ADRO","AMRT","ANTM","ARTO","ASII","BBCA","BBNI","BBRI","BMRI",
    "BRPT","BUKA","CPIN","GOTO","INCO","INDF","INTP","KLBF","MDKA","MEDC",
    "MYOR","PGEO","PTBA","SMGR","SRTG","TBIG","TLKM","TOWR","TPIA","UNTR"
]

perusahaan = st.selectbox("Pilih Perusahaan", lq45)

# =========================
# Load Excel (AMAN)
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = "Data Saham Prakbigdata (1).xlsx"


df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()

# =========================
# Filter data
# =========================
data_perusahaan = df[df["Perusahaan"] == perusahaan]

st.subheader("📈 Data Nilai")

if not data_perusahaan.empty:
    st.dataframe(data_perusahaan[["Tanggal", "Nilai"]])
else:
    st.warning("Data perusahaan tidak ditemukan di Excel")
