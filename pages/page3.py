import streamlit as st
import pandas as pd

st.title("📉 Analisis Data Historis Saham")

uploaded_file = st.file_uploader(
    "Upload file Excel Data Saham",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

df = pd.read_excel("Data Saham Prakbigdata.csv  BARU.xlsx", header=1)


    # Kolom saham (selain tanggal)
    saham_list = df.columns[1:]

    saham = st.selectbox(
        "Pilih Saham Perusahaan",
        options=saham_list
    )

    st.subheader(f"📈 Grafik Harga Saham {saham}")

    chart_data = df[[tanggal_col, saham]].dropna()
    chart_data = chart_data.set_index(tanggal_col)

    st.line_chart(chart_data)

    # Analisis sederhana
    harga_awal = chart_data[saham].iloc[0]
    harga_akhir = chart_data[saham].iloc[-1]
    perubahan = harga_akhir - harga_awal
    persentase = (perubahan / harga_awal) * 100

    st.subheader("📝 Penjelasan")

    if perubahan > 0:
        tren = "mengalami tren kenaikan"
    else:
        tren = "mengalami tren penurunan"

    st.write(
        f"""
        Berdasarkan data historis, harga saham **{saham}**
        {tren} selama periode pengamatan.

        Harga awal tercatat sekitar **{harga_awal:.2f}**
        dan harga akhir sebesar **{harga_akhir:.2f}**.
        Perubahan harga sebesar **{perubahan:.2f}**
        atau **{persentase:.2f}%**.
        """
    )

else:
    st.info("Silakan upload file Excel terlebih dahulu.")
