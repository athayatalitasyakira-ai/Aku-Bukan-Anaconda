import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Saham",
    layout="wide"
)

st.title("📈 Visualisasi Data Saham")

FILE_PATH = "Data Saham Prakbigdata.csv  BARU.xlsx"

@st.cache_data
def load_data():
    df_raw = pd.read_excel(FILE_PATH, header=None)

    header_row = None
    for i in range(min(5, len(df_raw))):
        row = df_raw.iloc[i].astype(str).str.lower()
        if row.str.contains("tanggal").any():
            header_row = i
            break

    if header_row is not None:
        df = pd.read_excel(FILE_PATH, header=header_row)
    else:
        df = pd.read_excel(FILE_PATH, header=0)

    return df

df = load_data()

df.columns = df.columns.astype(str).str.strip()

if all(col.startswith("Unnamed") for col in df.columns):
    df.columns = [
        "Tanggal", "Kode", "Open", "High", "Low",
        "Close", "Volume", "Adj Close",
        "Kolom8", "Kolom9", "Kolom10", "Kolom11"
    ]
required_cols = ["Tanggal", "Kode"]
missing = [c for c in required_cols if c not in df.columns]

if missing:
    st.error(f"Kolom wajib tidak ditemukan: {missing}")
    st.write("Kolom tersedia:", df.columns)
    st.stop()
df["Tanggal"] = pd.to_datetime(df["Tanggal"], errors="coerce")
df = df.dropna(subset=["Tanggal"])
st.sidebar.header("Filter")

saham_list = sorted(df["Kode"].dropna().unique())

if len(saham_list) == 0:
    st.error("Data saham kosong")
    st.stop()

selected_saham = st.sidebar.selectbox(
    "Pilih Kode Saham",
    options=saham_list
)
df_saham = df[df["Kode"] == selected_saham]
st.subheader(f"Data Saham: {selected_saham}")
st.dataframe(df_saham, use_container_width=True)
if "Close" in df_saham.columns:
    st.line_chart(
        df_saham.set_index("Tanggal")["Close"]
    )
else:
    st.warning("Kolom Close tidak tersedia")
