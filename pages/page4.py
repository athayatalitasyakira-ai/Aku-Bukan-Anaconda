 HEAD

import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, Dropdown
from datetime import datetime, timedelta
<<<<<<< HEAD

def excel_serial_to_date(serial):
    if isinstance(serial, (int, float)):
        base_date = datetime(1899, 12, 30)  # Base date untuk Excel
        return base_date + timedelta(days=serial)
    else:
        # Jika sudah dalam format string seperti '01/02/2025', parse langsung
        try:
            return pd.to_datetime(serial, format='%m/%d/%Y')
        except:
            return pd.NaT  # Jika gagal, return NaT
# Baca file Excel (asumsikan file ada di direktori yang sama atau sesuaikan path)
file_path = 'Data Harga Saham Prakbigdata.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Bersihkan kolom Tanggal
df['Tanggal'] = df['Tanggal'].apply(excel_serial_to_date)

# Hapus baris dengan tanggal NaT jika ada
df = df.dropna(subset=['Tanggal'])

# Sortir berdasarkan tanggal
df = df.sort_values('Tanggal').reset_index(drop=True)

# Opsi saham yang tersedia (kolom selain Tanggal)
saham_options = ['Composite_Index', 'LQ45', 'IDX30']

# Fungsi untuk plot grafik dan tampilkan penjelasan
def plot_saham(saham):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Tanggal'], df[saham], marker='o', linestyle='-', color='b')
    plt.title(f'Data Historis Saham: {saham}')
    plt.xlabel('Tanggal')
    plt.ylabel('Harga')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
# Penjelasan di bawah grafik
    print(f"\nPenjelasan Grafik untuk {saham}:")
    print("Grafik ini menampilkan data historis harga saham dari tanggal terendah hingga tertinggi.")
    print(f"Data dimulai dari {df['Tanggal'].min().strftime('%Y-%m-%d')} hingga {df['Tanggal'].max().strftime('%Y-%m-%d')}.")
    print(f"Harga terendah: {df[saham].min():.2f}")
    print(f"Harga tertinggi: {df[saham].max():.2f}")
    print(f"Rata-rata harga: {df[saham].mean():.2f}")
    print("Anda dapat menganalisis tren naik-turun harga saham berdasarkan grafik ini.")

# Buat dropdown interaktif
interact(plot_saham, saham=Dropdown(options=saham_options, description='Pilih Saham:'));
=======
 69436736987791aa93a728a773631f3e54fbd1f0
>>>>>>> debd6586cc6867eb143bc7352253bfcdc49bcfed
