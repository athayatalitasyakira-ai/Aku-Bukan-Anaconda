import streamlit as st
import pandas as pd
from docx import Document

st.title("📊 Informasi Perusahaan LQ45")

# =========================
# List Perusahaan LQ45
# =========================
lq45 = [
    "AADI","ADRO","AMRT","ANTM","ARTO","ASII","BBCA","BBNI","BBRI","BMRI",
    "BRPT","BUKA","CPIN","GOTO","INCO","INDF","INTP","KLBF","MDKA","MEDC",
    "MYOR","PGEO","PTBA","SMGR","SRTG","TBIG","TLKM","TOWR","TPIA","UNTR"
]

# =========================
# Pilih Perusahaan
# =========================
perusahaan = st.selectbox("Pilih Perusahaan", lq45)

# =========================
# Load Excel
# =========================
df = pd.read_excel("Data Saham Prakbigdata.xlsx")
df.columns = df.columns.str.strip()

# =========================
# Load Word
# =========================
doc = Document("INFORMASI.docx")

info_text = ""
for para in doc.paragraphs:
    if para.text.startswith(perusahaan):
        info_text = para.text
        break

# =========================
# Tampilkan Informasi Perusahaan
# =========================
st.subheader("📄 Informasi Perusahaan")
if info_text:
    st.write(info_text)
else:
    st.warning("Informasi perusahaan tidak ditemukan di file Word")

# =========================
# Filter Data Excel
# =========================
data_perusahaan = df[df["Perusahaan"] == perusahaan]

st.subheader("📈 Data Perusahaan")
if not data_perusahaan.empty:
    st.dataframe(data_perusahaan)
else:
    st.warning("Data perusahaan tidak ditemukan di Excel")
