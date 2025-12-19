import streamlit as st

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


data_indeks["LQ45"]["ASII"] = {
    "nama": "PT Astra International Tbk",
    "sektor": "Otomotif",
    "harga": "Rp 6.300",
    "market_cap": "Rp 255 T",
    "tahun": 1957,
    "deskripsi": "Konglomerasi besar Indonesia."
}
