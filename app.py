import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Home", icon="🐊"),
    st.Page(page="pages/page3.py", title="Grafik", icon="🦚"),
    st.Page(page="pages/page4.py", title="Perbandingan", icon="🐢").
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
