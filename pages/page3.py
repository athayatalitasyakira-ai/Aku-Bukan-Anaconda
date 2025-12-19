import streamlit as st
import pandas as pd

st.set_page_config(page_title="Grafik Data Saham", layout="wide")

st.title("📈 Grafik Data Saham")

@st.cache_data
def load_data():
    return pd.read_excel("Data Saham Prakbigdata.xlsx")

try:
    df = load_data()
    st.success("Data berhasil dimuat")

    # Tampilkan data
    st.subheader("Preview Data")
    st.dataframe(df)

    # Pilih kolom numerik untuk grafik
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) > 0:
        col = st.selectbox("Pilih kolom untuk grafik", numeric_cols)

        st.subheader(f"Grafik {col}")
        st.line_chart(df[col])
    else:
        st.warning("Tidak ada kolom numerik untuk dibuat grafik")

except Exception as e:
    st.error("Gagal membuka file data")
    st.code(str(e))
