import streamlit as st
import pandas as pd
from pathlib import Path
import os



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
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "data_saham.xlsx")

# 1️⃣ BACA FILE DULU
df = pd.read_excel(file_path)

# 2️⃣ (OPSIONAL) BERSIHKAN NAMA KOLOM
df.columns = df.columns.str.strip()

# 3️⃣ BARU BOLEH PAKAI df
st.write("Kolom di dataset:")
st.write(df.columns.tolist())

# 4️⃣ CONTOH PEMAKAIAN
perusahaan = st.selectbox("Pilih perusahaan", df["Perusahaan"].unique())
data_perusahaan = df[df["Perusahaan"] == perusahaan]

st.dataframe(data_perusahaan)
❗ KESALAHAN YANG SERING TERJADI
❌ Ini SALAH:

python
Copy code
st.write(df.columns.tolist())
df = pd.read_excel(file_path)
❌ Ini juga SALAH:

python
Copy code
if uploaded_file:
    df = pd.read_excel(uploaded_file)

st.write(df.columns.tolist())  # df belum tentu ada
✅ JIKA PAKAI file_uploader
WAJIB pakai if:

python
Copy code
uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(data_saham_baru)
    st.write(df.columns.tolist())
🧠 RINGKASAN
Masalah	Penyebab
df undefined	Urutan kode salah
Streamlit error	❌
Pandas error	❌

🚀 LANGKAH TERAKHIR
Pastikan df = pd.read_excel(...) ADA

Pastikan st.write(df...) di BAWAHNYA

Save → Restart Streamlit

Kalau mau, kirimkan isi page2.py sekarang,
aku rapikan sampai tidak ada satu pun error 🔥







