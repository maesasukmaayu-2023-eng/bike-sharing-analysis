# Bike Sharing Data Analysis Dashboard
# Deskripsi
Proyek ini bertujuan untuk menganalisis pola dan tren penyewaan sepeda berdasarkan waktu serta faktor cuaca. Analisis difokuskan pada dua hal utama, yaitu tren penyewaan sepeda per jam dan harian pada periode tahun 2011–2012, serta pengaruh faktor cuaca seperti suhu, kelembaban, dan kecepatan angin terhadap jumlah penyewaan. Selain itu, proyek ini juga mengeksplorasi pola penggunaan sepeda sepanjang hari dan mengidentifikasi waktu puncak penggunaan bagi pengguna casual dan registered. Hasil analisis divisualisasikan dalam bentuk dashboard interaktif menggunakan Streamlit untuk memudahkan eksplorasi data.


# Fitur Dashboard
Visualisasi tren penyewaan sepeda harian, Analisis pola penyewaan per jam, Perbandingan pengguna casual dan registered, Visualisasi pengaruh faktor cuaca terhadap jumlah penyewaan, Filter interaktif berdasarkan rentang waktu  

# Setup Environment - Anaconda
conda create --name main-ds python=3.14
conda activate main-ds
pip install -r requirements.txt

# Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

# Run steamlit app
streamlit run Dashboard/Dashboard.py