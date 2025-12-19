import streamlit as st
import pandas as pd

st.title("📊 Data Saham (Tanpa File)")

df = pd.DataFrame({
    "Perusahaan": ["BBCA", "BBRI", "TLKM", "BMRI"],
    "Harga": [9800, 5200, 4100, 6100],
    "Volume": [120000, 150000, 100000, 130000]
})

st.success("✅ Data berhasil dimuat")

# Pilih perusahaan
perusahaan = st.selectbox(
    "Pilih Perusahaan",
    df["Perusahaan"].unique()
)

# Filter data
data_perusahaan = df[df["Perusahaan"] == perusahaan]

st.subheader("📈 Detail Saham")
st.dataframe(data_perusahaan)
