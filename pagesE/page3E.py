import streamlit as st
import pandas as pd

st.set_page_config(page_title="Grafik Data Saham", layout="wide")

st.title("📈 Grafik Data Saham")

@st.cache_data
def load_data():
    return pd.read_excel("Data Saham Prakbigdata.xlsx")

try:
    df = load_data()
    st.success("Data berhasil dimuat")

    # Tampilkan data
    st.subheader("Preview Data")
    st.dataframe(df)

    # Pilih kolom numerik untuk grafik
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) > 0:
        col = st.selectbox("Pilih kolom untuk grafik", numeric_cols)

        st.subheader(f"Grafik {col}")
        st.line_chart(df[col])
    else:
        st.warning("Tidak ada kolom numerik untuk dibuat grafik")

except Exception as e:
    st.error("Gagal membuka file data")
    st.code(str(e))




st.title("Analisis Data Harga Saham")
st.write("Data ini berisi pergerakan indeks saham di Indonesia.")

# ANALISIS UMUM
st.subheader("1. Gambaran Umum Data")
st.write("""
Data yang dianalisis merupakan data **time series** harga saham
yang terdiri dari:
- **Composite Index (IHSG)** sebagai indikator pasar secara keseluruhan
- **LQ45** yang mewakili saham paling likuid
- **IDX30** yang mewakili saham berkapitalisasi besar


st.subheader("2. Statistik Deskriptif")
st.write(
Berdasarkan statistik deskriptif, dapat disimpulkan bahwa:
IHSG memiliki nilai rata-rata paling tinggi karena mencerminkan agregasi seluruh saham.
LQ45 menunjukkan fluktuasi yang lebih besar dibanding IDX30.
IDX30 relatif lebih stabil karena berisi saham-saham unggulan (blue chip).
    )
st.write(data.describe())


st.subheader("3. Analisis Pergerakan Indeks")
st.write(
Pergerakan ketiga indeks menunjukkan **pola yang cenderung searah**.
Hal ini menandakan adanya korelasi positif antar indeks saham.

Saat IHSG mengalami penurunan, LQ45 biasanya turun lebih tajam.
IDX30 cenderung mengalami perubahan yang lebih kecil,
  menunjukkan tingkat risiko yang lebih rendah.
)


st.subheader("4. Analisis Risiko dan Volatilitas")
st.write(
Dari pola pergerakan data:
LQ45  memiliki volatilitas paling tinggi sehingga cocok bagi investor agresif.
IHSG mencerminkan kondisi pasar secara umum.
IDX30 lebih stabil dan cocok untuk investasi jangka menengah hingga panjang.
)


st.subheader("5. Kesimpulan")
st.write(
Berdasarkan hasil analisis data Excel:
Ketiga indeks saham bergerak searah dan saling memengaruhi.
LQ45 paling sensitif terhadap perubahan kondisi pasar.
IDX30 menunjukkan stabilitas tertinggi.
Data ini dapat digunakan sebagai dasar pengambilan keputusan investasi
   maupun analisis kondisi pasar modal Indonesia.
)