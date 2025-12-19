import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Saham", layout="wide")
st.title("📈 Visualisasi Data Saham")

FILE_PATH = "Data Saham Prakbigdata.csv  BARU.xlsx"

# =========================
# 1. LOAD DATA (PASTI AMAN)
# =========================
@st.cache_data
def load_data():
    return pd.read_excel(FILE_PATH, header=None)

df = load_data()

# =========================
# 2. RENAME KOLOM LANGSUNG
# =========================
df.columns = [
    "Tanggal", "Kode", "Open", "High", "Low",
    "Close", "Volume", "Adj Close",
    "Kolom8", "Kolom9", "Kolom10", "Kolom11"
]

# =========================
# 3. VALIDASI JUMLAH KOLOM
# =========================
if df.shape[1] < 7:
    st.error("Struktur kolom tidak sesuai")
    st.write(df.head())
    st.stop()

# =========================
# 4. PARSING TANGGAL (AMAN)
# =========================
df["Tanggal"] = pd.to_datetime(df["Tanggal"], errors="coerce")
df = df.dropna(subset=["Tanggal"])


st.sidebar.header("Filter Saham")

saham_list = sorted(df["Kode"].dropna().unique())

if len(saham_list) == 0:
    st.error("Data saham kosong")
    st.stop()

selected_saham = st.sidebar.selectbox(
    "Pilih Kode Saham",
    saham_list
)


df_saham = df[df["Kode"] == selected_saham]

# =========================
# 7. TAMPILKAN DATA
# =========================
st.subheader(f"Data Saham: {selected_saham}")
st.dataframe(df_saham, use_container_width=True)

# =========================
# 8. GRAFIK
# =========================
st.line_chart(
    df_saham.set_index("Tanggal")["Close"]
)
