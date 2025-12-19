import streamlit as st
import pandas as pd

st.title("📈 Analisis Data Historis Saham")

uploaded_file = st.file_uploader(
    "Upload file Excel data saham",
    type=["xlsx"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Kolom pertama = tanggal
    kolom_tanggal = df.columns[0]
    df[kolom_tanggal] = pd.to_datetime(df[kolom_tanggal])

    # Pilih saham
    saham = st.selectbox(
        "Pilih Saham Perusahaan",
        options=df.columns[1:]
    )

    # Paksa numerik
    df[saham] = pd.to_numeric(df[saham], errors="coerce")

    # Siapkan data grafik (INI KUNCI)
    chart_df = df[[kolom_tanggal, saham]].dropna()
    chart_df = chart_df.set_index(kolom_tanggal)

    # Grafik (AMAN)
    st.subheader(f"📊 Grafik Historis Harga Saham {saham}")
    st.line_chart(chart_df)

    # Analisis
    data_saham = chart_df[saham]

    harga_awal = data_saham.iloc[0]
    harga_akhir = data_saham.iloc[-1]
    perubahan = harga_akhir - harga_awal
    persentase = (perubahan / harga_awal) * 100
    volatilitas = data_saham.std()

    st.subheader("📝 Penjelasan Data Historis")

    if perubahan > 0:
        tren = "mengalami tren kenaikan"
    elif perubahan < 0:
        tren = "mengalami tren penurunan"
    else:
        tren = "cenderung stagnan"

    st.write(f"""
    Berdasarkan data historis yang ditampilkan, harga saham **{saham}**
    {tren} selama periode pengamatan.

    Pada awal periode, harga saham berada di kisaran **{harga_awal:.2f}**,
    dan pada akhir periode tercatat sebesar **{harga_akhir:.2f}**.
    Hal ini menunjukkan perubahan harga sebesar **{perubahan:.2f}**
    atau sekitar **{persentase:.2f}%**.

    Tingkat volatilitas saham sebesar **{volatilitas:.2f}**, yang
    mencerminkan tingkat fluktuasi harga saham selama periode tersebut.
    Semakin tinggi volatilitas, semakin besar risiko pergerakan harga saham.
    """)

else:
    st.info("Silakan upload file Excel terlebih dahulu.")
