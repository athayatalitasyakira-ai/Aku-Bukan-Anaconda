import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Analisis Saham",
    layout="centered"
)

st.title("📊 Analisis Data Historis Saham")
st.write(
    "Pilih saham perusahaan untuk melihat grafik harga historis "
    "beserta penjelasan pergerakan harganya."
)

# Upload file Excel
uploaded_file = st.file_uploader(
    "📂 Upload File Excel Data Saham",
    type=["xlsx"]
)

if uploaded_file is not None:
    # Baca data
    df = pd.read_excel(uploaded_file)

    # Konversi kolom tanggal
    df["Tanggal"] = pd.to_datetime(df["Tanggal"])

    # Pilih saham
    saham = st.selectbox(
        "📌 Pilih Saham Perusahaan",
        options=df.columns[1:]
    )

    # Grafik
    st.subheader(f"📈 Grafik Historis Harga Saham {saham}")
    st.line_chart(
        df.set_index("Tanggal")[saham]
    )

    # Analisis sederhana
    data_saham = df[saham].dropna()

    harga_awal = data_saham.iloc[0]
    harga_akhir = data_saham.iloc[-1]
    perubahan = harga_akhir - harga_awal
    persentase = (perubahan / harga_awal) * 100
    volatilitas = data_saham.std()

    tren = "mengalami tren kenaikan" if perubahan > 0 else "mengalami tren penurunan"

    # Penjelasan
    st.subheader("📝 Penjelasan Data Historis Saham")

    st.write(f"""
    Berdasarkan data historis yang ditampilkan, harga saham **{saham}**
    {tren} selama periode pengamatan.

    Pada awal periode, harga saham tercatat sebesar **{harga_awal:.2f}**,
    sedangkan pada akhir periode mencapai **{harga_akhir:.2f}**.
    Dengan demikian, terjadi perubahan harga sebesar **{perubahan:.2f}**
    atau sekitar **{persentase:.2f}%**.

    Nilai volatilitas saham sebesar **{volatilitas:.2f}** menunjukkan
    tingkat fluktuasi harga selama periode tersebut. Semakin tinggi
    volatilitas, maka risiko pergerakan harga saham semakin besar.
    """)

else:
    st.info("Silakan upload file Excel terlebih dahulu.")
