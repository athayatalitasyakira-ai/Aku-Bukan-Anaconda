import streamlit as st

# ==========================
# DATA SAHAM (SUMBER DATA)
# ==========================
data_indeks = {
    "Composite Index (IHSG)": {
        "BBCA": {
            "nama": "PT Bank Central Asia Tbk",
            "sektor": "Perbankan",
            "harga": "Rp 9.750",
            "market_cap": "Rp 1.200 Triliun",
            "tahun": 1957,
            "deskripsi": "Bank swasta terbesar di Indonesia."
        },
        "TLKM": {
            "nama": "PT Telkom Indonesia Tbk",
            "sektor": "Telekomunikasi",
            "harga": "Rp 4.200",
            "market_cap": "Rp 415 Triliun",
            "tahun": 1965,
            "deskripsi": "Perusahaan telekomunikasi BUMN."
        }
    },

    "LQ45": {
        "BBRI": {
            "nama": "PT Bank Rakyat Indonesia Tbk",
            "sektor": "Perbankan",
            "harga": "Rp 5.150",
            "market_cap": "Rp 780 Triliun",
            "tahun": 1895,
            "deskripsi": "Fokus pembiayaan UMKM."
        },
        "ASII": {
            "nama": "PT Astra International Tbk",
            "sektor": "Otomotif",
            "harga": "Rp 6.300",
            "market_cap": "Rp 255 Triliun",
            "tahun": 1957,
            "deskripsi": "Konglomerasi multinasional Indonesia."
        }
    },

    "IDX30": {
        "BMRI": {
            "nama": "PT Bank Mandiri Tbk",
            "sektor": "Perbankan",
            "harga": "Rp 6.100",
            "market_cap": "Rp 570 Triliun",
            "tahun": 1998,
            "deskripsi": "Bank BUMN terbesar berdasarkan aset."
        }
    }
}

# ==========================
# TAMPILAN PAGE 4
# ==========================
st.title("📊 Page 4 – Informasi Saham")
st.write("Pilih indeks dan saham untuk melihat informasi lengkap perusahaan")

# ==========================
# PILIH INDEKS
# ==========================
indeks = st.selectbox(
    "📌 Pilih Indeks Saham",
    list(data_indeks.keys())
)

# ==========================
# PILIH SAHAM
# ==========================
kode_saham = st.selectbox(
    "📈 Pilih Kode Saham",
    list(data_indeks[indeks].keys())
)

# ==========================
# TAMPILKAN DATA
# ==========================
saham = data_indeks[indeks][kode_saham]

st.markdown("---")
st.subheader(f"🏢 {saham['nama']} ({kode_saham})")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏭 Informasi Perusahaan")
    st.write(f"*Sektor:* {saham['sektor']}")
    st.write(f"*Tahun Berdiri:* {saham['tahun']}")
    st.write(f"*Deskripsi:* {saham['deskripsi']}")

with col2:
    st.markdown("### 💰 Informasi Saham")
    st.write(f"*Harga Saham:* {saham['harga']}")
    st.write(f"*Kapitalisasi Pasar:* {saham['market_cap']}")
