import streamlit as st
import pandas as pd

st.title("📊 Nilai Saham Perusahaan LQ45")

# =========================
# List Perusahaan LQ45
# =========================
lq45 = [
    "AADI","ADRO","AMRT","ANTM","ARTO","ASII","BBCA","BBNI","BBRI","BMRI",
    "BRPT","BUKA","CPIN","GOTO","INCO","INDF","INTP","KLBF","MDKA","MEDC",
    "MYOR","PGEO","PTBA","SMGR","SRTG","TBIG","TLKM","TOWR","TPIA","UNTR"
]

# =========================
# Dropdown pilihan perusahaan
# =========================
perusahaan = st.selectbox("Pilih Perusahaan", lq45)

# =========================
# Load Excel
# =========================
df = pd.read_excel("Data Saham Prakbigdata (1).xlsx")
df.columns = df.columns.str.strip()

# =========================
# Filter data sesuai pilihan
# =========================
data_perusahaan = df[df["Perusahaan"] == perusahaan]

# =========================
# Tampilkan Nilai
# =========================
st.subheader("📈 Data Nilai")

if not data_perusahaan.empty:
    st.dataframe(data_perusahaan[["Tanggal", "Nilai"]])
else:
    st.warning("Data perusahaan tidak ditemukan di Excel")
