import streamlit as st
import pandas as pd

st.title("📉 Analisis Data Historis Saham")
st.write("Pilih saham untuk melihat pergerakan harga historis dan penjelasannya.")
uploaded_file = st.file_uploader(
    "Upload file Excel Data Saham",
    type=["xlsx"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
     df["Tanggal"] = pd.to_datetime(df["Tanggal"])
saham = st.selectbox(
        "Pilih Saham Perusahaan",
        options=df.columns[1:]
    )

 st.subheader(f"📈 Grafik Historis Harga Saham {saham}")
    st.line_chart(
        df.set_index("Tanggal")[saham]
    )
    data_saham = df[saham].dropna()

    harga_awal = data_saham.iloc[0]
    harga_akhir = data_saham.iloc[-1]
    perubahan = harga_akhir - harga_awal
    persentase = (perubahan / harga_awal) * 100
    volatilitas = data_saham.std()

    st.subheader("📝 Penjelasan Data Historis")

    if perubahan > 0:
        tren = "mengalami tren kenaikan"
    else:
        tren = "mengalami tren penurunan"

    st.write(f"""
    Berdasarkan data historis yang ditampilkan, harga saham **{saham}**
    {tren} selama periode pengamatan.

    Pada awal periode, harga saham berada di kisaran **{harga_awal:.2f}**,
    dan pada akhir periode tercatat sebesar **{harga_akhir:.2f}**.
    Hal ini menunjukkan perubahan harga sebesar **{perubahan:.2f}**
    atau sekitar **{persentase:.2f}%**.

    Tingkat volatilitas saham ini tergolong **{volatilitas:.2f}**,
    yang mencerminkan tingkat fluktuasi harga saham selama periode tersebut.
    Semakin tinggi nilai volatilitas, semakin besar risiko pergerakan harga saham.
    """)

else:
    st.info("Silakan upload file Excel terlebih dahulu.")