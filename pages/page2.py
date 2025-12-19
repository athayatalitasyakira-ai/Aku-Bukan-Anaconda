import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

# ==========================
# TEMPAT MENYIMPAN DATA
# ==========================
data_indeks = {
    "Composite Index (IHSG)": {
        "BBCA": {
            "nama": "PT Bank Central Asia Tbk",
            "sektor": "Perbankan",
            "harga": "Rp 9.750",
            "market_cap": "Rp 1.200 T",
            "tahun": 1957,
            "deskripsi": "Bank swasta terbesar di Indonesia."
        },
        "TLKM": {
            "nama": "PT Telkom Indonesia Tbk",
            "sektor": "Telekomunikasi",
            "harga": "Rp 4.200",
            "market_cap": "Rp 415 T",
            "tahun": 1965,
            "deskripsi": "Perusahaan telekomunikasi milik negara."
        }
    },

    "LQ45": {
        "BBRI": {
            "nama": "PT Bank Rakyat Indonesia Tbk",
            "sektor": "Perbankan",
            "harga": "Rp 5.150",
            "market_cap": "Rp 780 T",
            "tahun": 1895,
            "deskripsi": "Bank fokus pembiayaan UMKM."
        },
        "ASII": {
            "nama": "PT Astra International Tbk",
            "sektor": "Otomotif",
            "harga": "Rp 6.300",
            "market_cap": "Rp 255 T",
            "tahun": 1957,
            "deskripsi": "Konglomerasi multinasional Indonesia."
        }
    },

    "IDX30": {
        "BMRI": {
            "nama": "PT Bank Mandiri Tbk",
            "sektor": "Perbankan",
            "harga": "Rp 6.100",
            "market_cap": "Rp 570 T",
            "tahun": 1998,
            "deskripsi": "Bank BUMN terbesar berdasarkan aset."
        }
    }
}

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Informasi Saham Indonesia",
    layout="wide"
)

st.title("📊 Dashboard Informasi Saham")
st.caption("Pilih indeks dan saham untuk melihat detail perusahaan")

# ==========================
# PILIH INDEKS
# ==========================
indeks = st.selectbox(
    "📌 Pilih Indeks Saham",
    options=list(data_indeks.keys())
)

# ==========================
# PILIH SAHAM
# ==========================
kode_saham = st.selectbox(
    "📈 Pilih Kode Saham",
    options=list(data_indeks[indeks].keys())
)

# ==========================
# TAMPILKAN INFORMASI
# ==========================
if kode_saham:
    saham = data_indeks[indeks][kode_saham]

    st.subheader(f"🏢 {saham['nama']} ({kode_saham})")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🏭 Informasi Perusahaan")
        st.write(f"**Sektor:** {saham['sektor']}")
        st.write(f"**Tahun Berdiri:** {saham['tahun']}")
        st.write(f"**Deskripsi:** {saham['deskripsi']}")

    with col2:
        st.markdown("### 💰 Informasi Saham")
        st.write(f"**Harga Saham:** {saham['harga']}")
        st.write(f"**Kapitalisasi Pasar:** {saham['market_cap']}")

    st.markdown("---")
    st.success("Data saham berhasil ditampilkan ✅")
