import streamlit as st
import pandas as pd

st.title("📈 Analisis Data Historis Saham")

st.write("Pilih perusahaan saham untuk melihat grafik historis dan penjelasannya.")

uploaded_file = st.file_uploader(
    "Upload file Excel data saham",
    type=["xlsx"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Gunakan kolom pertama sebagai tanggal (AMAN)
    kolom_tanggal = df.columns[0]
    df[kolom_tanggal] = pd.to_datetime(df[kolom_tanggal])

    # Pilih saham dari kolom yang tersedia
    saham = st.selectbox(
        "Pilih Saham Perusahaan",
        options=df.columns[1:]
    )

# Pastikan data saham numerik
df[saham] = pd.to_numeric(df[saham], errors="coerce")

st.line_chart(
    df.set_index(kolom_tanggal)[saham]
)

    # Analisis sederhana
    data_saham = df[saham].dropna()

    harga_awal = data_saham.iloc[0]
    harga_akhir = data_saham.iloc[-1]
    perubahan = harga_akhir - harga_awal
    persentase = (perubahan / harga_awal) * 100
    volatilitas = data_saham.std()

    # Penjelasan
    st.subheader("📝 Penjelasan Data Historis Saham")

    if perubahan > 0:
        tren = "mengalami tren kenaikan"
    elif perubahan < 0:
        tren = "mengalami tren penurunan"
    else:
        tren = "cenderung stagnan"

    st.write(f"""
    Berdasarkan data historis yang ditampilkan, harga saham **{saham}**
    {tren} selama periode pengamatan.

    Pada awal periode, harga saham tercatat sebesar **{harga_awal:.2f}**,
    dan pada akhir periode mencapai **{harga_akhir:.2f}**.
    Hal ini menunjukkan perubahan harga sebesar **{perubahan:.2f}**
    atau sekitar **{persentase:.2f}%**.

    Tingkat volatilitas saham ini sebesar **{volatilitas:.2f}**, yang
    mencerminkan tingkat fluktuasi harga saham selama periode tersebut.
    Semakin tinggi volatilitas, maka semakin besar risiko dan peluang
    pergerakan harga saham.
    """)

else:
    st.info("Silakan upload file Excel terlebih dahulu.")

