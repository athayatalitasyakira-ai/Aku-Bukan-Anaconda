import streamlit as st
import pandas as pd

# ======================
# Judul Aplikasi
# ======================
st.set_page_config(page_title="Data Perusahaan", layout="wide")
st.title("📊 Data Perusahaan")

# ======================
# Load Data (AMAN)
# ======================
@st.cache_data
def load_data():
    df = pd.read_excel(
        "Data Saham Prakbigdata.csv  BARU.xlsx",
        header=None
    )

    df.columns = [
        "Tanggal", "Kode", "Open", "High", "Low",
        "Close", "Volume", "Adj Close",
        "Kolom8", "Kolom9", "Kolom10", "Kolom11"
    ]

    # Ubah kolom tanggal
    df["Tanggal"] = pd.to_datetime(df["Tanggal"], errors="coerce")
    df = df.dropna(subset=["Tanggal"])

    return df

df = "Data_saham_Prakbogdata_BARU.xlsx"

# ======================
# Pilih Perusahaan
# ======================
st.sidebar.header("Pilih Perusahaan")

perusahaan = sorted(df["Kode"].dropna().unique())

kode = st.sidebar.selectbox(
    "Kode Perusahaan",
    perusahaan
)

# ======================
# Filter Data
# ======================
df_perusahaan = df[df["Kode"] == kode]

# ======================
# Tampilkan Data
# ======================
st.subheader(f"📋 Data Perusahaan: {kode}")
st.dataframe(df_perusahaan, use_container_width=True)

# ======================
# Grafik Harga
# ======================
st.subheader("📈 Grafik Harga Penutupan")

st.line_chart(
    df_perusahaan.set_index("Tanggal")["Close"]
)
