import streamlit as st
import pandas as pd
import os

st.title("Perbandingan Saham")

BASE_DIR = os.getcwd()
FILE_PATH = os.path.join(BASE_DIR, "data", "data_saham_baru.xlsx")

if not os.path.exists(FILE_PATH):
    st.error("File Excel tidak ditemukan")
    st.stop()

df = pd.read_excel(FILE_PATH, engine="openpyxl")

st.subheader("📌 Data Perbandingan")
st.dataframe(df.head())  # tampilkan contoh data
