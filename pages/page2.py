import streamlit as st
import pandas as pd
from docx import Document

# ===============================
# FUNGSI BACA DATA WORD
# ===============================
def load_word_info(file_path):
    doc = Document(file_path)
    data = {}

    for para in doc.paragraphs:
        text = para.text.strip()
        if "(" in text and ":" in text:
            kode = text.split("(")[0].strip("- ").strip()
            deskripsi = text.split("):")[-1].strip()
            data[kode] = deskripsi

    return data

# ===============================
# LOAD DATA
# ===============================
word_info = load_word_info("INFORMASI.docx")
excel_data = pd.read_excel("Data Saham Prakbigdata.csv  BARU.xlsx")

# Pastikan kolom kode saham ada
excel_data["Kode Saham"] = excel_data["Kode Saham"].str.upper()

# ===============================
# SETUP PAGE
# ===============================
st.set_page_config(
    page_title="Informasi Saham Indonesia",
    layout="wide"
)

st.title("📊 Informasi Saham Indonesia")
st.caption("Pilih saham untuk melihat informasi perusahaan & data saham")

# ===============================
# PILIH SAHAM
# ===============================
daftar_saham = sorted(word_info.keys())

kode_saham = st.selectbox(
    "📌 Pilih Kode Saham",
    daftar_saham
)

# ===============================
# TAMPILKAN INFORMASI
# ===============================
if kode_saham:
    st.markdown("---")
    st.subheader(f"🏢 {kode_saham}")

    col1, col2 = st.columns(2)

    # ===============================
    # INFORMASI PERUSAHAAN (WORD)
    # ===============================
    with col1:
        st.markdown("### 🏭 Informasi Perusahaan")
        st.write(word_info.get(kode_saham, "Data tidak tersedia"))

    # ===============================
    # INFORMASI SAHAM (EXCEL)
    # ===============================
    with col2:
        st.markdown("### 💰 Informasi Saham")

        data_saham = excel_data[
            excel_data["Kode Saham"] == kode_saham
        ]

        if not data_saham.empty:
            st.dataframe(data_saham, use_container_width=True)
        else:
            st.warning("Data saham tidak ditemukan di Excel")

    st.success("Data berhasil ditampilkan ✅")
