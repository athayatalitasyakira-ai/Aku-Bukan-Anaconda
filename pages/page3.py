import streamlit as st
import pandas as pd

st.title("Visualisasi Harga Saham")

uploaded_file = st.file_uploader(
    "Upload data saham", 
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    # Baca file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Tampilkan kolom untuk cek
    st.write("Kolom data:", df.columns.tolist())

    # WAJIB: pastikan nama kolom sesuai
    df["Tanggal"] = pd.to_datetime(df["Tanggal"])
    df = df.sort_values("Tanggal")

    # Jadikan Tanggal sebagai index
    df = df.set_index("Tanggal")

    # Pastikan kolom numerik
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    # Line chart (INI YANG BENAR)
    st.line_chart(df["Close"])

    # Penjelasan
    st.markdown("""
    **Penjelasan:**  
    Grafik di atas menunjukkan pergerakan harga penutupan (*closing price*) saham 
    berdasarkan waktu. Sumbu horizontal merepresentasikan tanggal perdagangan, 
    sedangkan sumbu vertikal menunjukkan nilai harga saham. Visualisasi ini membantu 
    pengguna untuk mengamati tren kenaikan atau penurunan harga saham dari waktu ke waktu.
    """)
