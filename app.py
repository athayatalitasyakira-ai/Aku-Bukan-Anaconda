import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Analisis Data Saham",
    layout="wide"
)

# Judul utama
st.title("📈 Analisis Data Saham")
st.write("Gunakan sidebar untuk memilih page.")

# NOTE:
# Semua file Python di folder 'pages/' otomatis muncul di sidebar sebagai page.
# Jadi tidak perlu membuat st.Page atau st.navigation sendiri.
