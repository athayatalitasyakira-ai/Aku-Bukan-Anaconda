import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("Grafik Saham")

BASE_DIR = os.getcwd()
FILE_PATH = os.path.join(BASE_DIR, "data", "data_saham_prakbigdata.xlsx")

if not os.path.exists(FILE_PATH):
    st.error("File Excel tidak ditemukan")
    st.stop()

df = pd.read_excel(FILE_PATH, engine="openpyxl")

st.subheader("📊 Grafik Harga Saham")
fig, ax = plt.subplots()
df.plot(y=df.columns[1], ax=ax)  # contoh plotting kolom kedua
st.pyplot(fig)
