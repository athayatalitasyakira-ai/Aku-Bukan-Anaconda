import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Saham", layout="wide")
st.title("📈 Visualisasi Data Saham")

FILE_PATH = "Data Saham Prakbigdata.csv  BARU.xlsx"

@st.cache_data
def load_data():
    return pd.read_excel("Data Saham Prakbigdata.csv BARU.xlsx" , header=None)

df = load_data()

# rename kolom langsung (ANTI KEYERROR)
df.columns = [
    "Tanggal", "Kode", "Open", "High", "Low",
    "Close", "Volume", "Adj Close",
    "C8", "C9", "C10", "C11"
]

# parsing tanggal aman
df["Tanggal"] = pd.to_datetime(df["Tanggal"], errors="coerce")
df = df.dropna(subset=["Tanggal"])

st.sidebar.header("Filter Saham")

saham_list = sorted(df["Kode"].dropna().unique())

selected = st.sidebar.selectbox(
    "Pilih Kode Saham",
    saham_list
)

df_saham = df[df["Kode"] == selected]

st.dataframe(df_saham, use_container_width=True)

st.line_chart(
    df_saham.set_index("Tanggal")["Close"]
)
