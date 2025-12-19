import streamlit as st
import pandas as pd

pages = [
    st.Page(page="pages/page1.py", title="Home", icon="🐊"),
    st.Page(page="pages/page2.py", title="Informasi", icon="🦕"),
    st.Page(page="pages/page3.py", title="Grafik", icon="🦚"),
    st.Page(page="pages/page4.py", title="Perbandingan", icon="🐢")
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()


st.set_page_config(
    page_title="Analisis Saham",
    layout="wide"
)

st.title("📊 Dashboard Analisis Saham")

st.write("""
Selamat datang di aplikasi analisis saham.

Gunakan menu **sidebar** untuk memilih halaman
dan melihat grafik serta analisis data saham.
""")
 

 (Update app.py dan page1, cleanup repository)
