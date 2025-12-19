import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Perbandingan Harga Saham", layout="wide")

st.title("📈 Perbandingan Harga Saham")
st.write("Visualisasi dan analisis data harga saham")

# ===============================
# LOAD DATA EXCEL (AMAN CLOUD)
# ===============================
file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Data Harga Saham Prakbigdata.xlsx"
)

try:
    df = pd.read_excel(file_path)
except FileNotFoundError:
    st.error("❌ File Excel tidak ditemukan. Pastikan sudah di-upload ke GitHub.")
    st.stop()

# ===============================
# PREVIEW DATA
# ===============================
st.subheader("📄 Preview Data")
st.dataframe(df, use_container_width=True)

# ===============================
# VALIDASI KOLOM
# ===============================
required_cols = ["Tanggal", "Kode_Saham", "Harga"]
for col in required_cols:
    if col not in df.columns:
        st.error(f"❌ Kolom '{col}' tidak ditemukan di data")
        st.stop()

df["Tanggal"] = pd.to_datetime(df["Tanggal"])

# ===============================
# FILTER SAHAM
# ===============================
st.subheader("🔎 Filter Saham")

list_saham = df["Kode_Saham"].unique().tolist()
selected_saham = st.multiselect(
    "Pilih Kode Saham",
    options=list_saham,
    default=list_saham[:2]
)

if not selected_saham:
    st.warning("⚠️ Pilih minimal 1 saham")
    st.stop()

df_filtered = df[df["Kode_Saham"].isin(selected_saham)]

# ===============================
# GRAFIK HARGA SAHAM
# ===============================
st.subheader("📊 Grafik Harga Saham")

st.line_chart(
    df_filtered,
    x="Tanggal",
    y="Harga",
    color="Kode_Saham"
)

# ===============================
# STATISTIK
# ===============================
st.subheader("📌 Statistik Harga Saham")

statistik = (
    df_filtered
    .groupby("Kode_Saham")["Harga"]
    .agg(["min", "max", "mean"])
    .reset_index()
)

st.dataframe(statistik, use_container_width=True)

# ===============================
# KESIMPULAN OTOMATIS
# ===============================
st.subheader("📝 Kesimpulan Singkat")

for _, row in statistik.iterrows():
    st.write(
        f"- Saham **{row['Kode_Saham']}** memiliki "
        f"harga terendah **{row['min']:.2f}**, "
        f"tertinggi **{row['max']:.2f}**, "
        f"dan rata-rata **{row['mean']:.2f}**"
    )