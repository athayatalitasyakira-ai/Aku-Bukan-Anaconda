import streamlit as st

st.title("📌 Langkah Mendapatkan Data Saham dari IDX")

st.markdown("""
Halaman ini menjelaskan cara memperoleh data saham dari website **IDX (Bursa Efek Indonesia)**
""")

st.header("📝 Langkah-Langkah")

st.markdown("""
### 1️⃣ Buka Website IDX
Buka link berikut:

👉 https://idx.co.id/id/data-pasar/laporan-statistik/digital-statistic/monthly/stock-price-index/daily-idx-indices?filter=eyJ5ZWFyIjoiMjAyNCIsIm1vbnRoIjoiMSIsInF1YXJ0ZXIiOjAsInR5cGUiOiJtb250aGx5In0%3D

---

### 2️⃣ Pilih Saham yang Dibutuhkan
Cari indeks / saham yang ingin dianalisis sesuai tugas.

---

### 3️⃣ Download Data
Pilih periode yang diperlukan (misalnya **harian**), lalu klik **Download**.

> Simpan file ke komputer.

---

### 4️⃣ Pindahkan Data ke Excel Baru
1. Buka **Excel baru**
2. Buka juga file hasil download IDX
3. Pindahkan:
   - **Tanggal**
   - **Data harga terakhir (Last / Close)**  
   saja ke Excel baru.

Pastikan tabel rapi dan tidak ada kolom kosong.

---

### 5️⃣ Data Siap Dipakai
Simpan file dengan nama yang diinginkan""")

