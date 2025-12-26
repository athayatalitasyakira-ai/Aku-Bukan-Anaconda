import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📊 Grafik Semua Saham")

FILE_PATH = "data/data_saham_prakbigdata.xlsx"

if not os.path.exists(FILE_PATH):
    st.error("❌ File Excel tidak ditemukan di folder data")
    st.stop()

df = pd.read_excel(FILE_PATH)
df.columns = df.columns.str.strip()

numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
if not numeric_cols:
    st.error("❌ Tidak ada kolom numeric untuk diplot")
    st.stop()

st.subheader("📈 Grafik Semua Saham (Interaktif)")

fig = px.line(
    df,
    x=df.index,
    y=numeric_cols,
    markers=True,
    title="Pergerakan Semua Saham"
)

fig.update_layout(
    xaxis_title="Index / Tanggal",
    yaxis_title="Harga Saham"
)

st.plotly_chart(fig, use_container_width=True)
