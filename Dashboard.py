import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Bike Sharing Analysis Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

all_df = load_data()

# ======================
# SIDEBAR (FILTER)
# ======================
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    st.header("Filter Data")
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data
main_df = all_df[
    (all_df["dteday"] >= pd.to_datetime(start_date)) &
    (all_df["dteday"] <= pd.to_datetime(end_date))
]

st.title("Bike Sharing Data Dashboard")

st.subheader("Tren Penyewaan Sepeda Harian")

daily_trend = main_df.groupby('dteday')['cnt'].sum().reset_index()

fig1, ax1 = plt.subplots(figsize=(12,5))
ax1.plot(daily_trend['dteday'], daily_trend['cnt'])
ax1.set_xlabel("Tanggal")
ax1.set_ylabel("Jumlah Penyewaan")
plt.xticks(rotation=45)

st.pyplot(fig1)

st.divider()

st.subheader("Pola Penyewaan Sepeda per Jam")

hourly_trend = main_df.groupby('hr')['cnt'].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10,5))
sns.lineplot(data=hourly_trend, x='hr', y='cnt', marker='o', ax=ax2)

ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Penyewaan")
ax2.set_xticks(range(0,24))

st.pyplot(fig2)

st.divider()

st.subheader("Pola Penggunaan: Casual vs Registered")

hourly_users = main_df.groupby('hr')[['casual', 'registered']].mean().reset_index()

fig3, ax3 = plt.subplots(figsize=(12,6))
sns.lineplot(data=hourly_users, x='hr', y='casual', label='Casual', marker='o', ax=ax3)
sns.lineplot(data=hourly_users, x='hr', y='registered', label='Registered', marker='o', ax=ax3)

ax3.set_xlabel("Jam")
ax3.set_ylabel("Rata-rata Penyewaan")

st.pyplot(fig3)

st.divider()

st.subheader("Pengaruh Faktor Cuaca terhadap Penyewaan")

fig4, ax4 = plt.subplots(figsize=(12,5))

sns.scatterplot(data=main_df, x='temp', y='cnt', label='Temp', ax=ax4)
sns.scatterplot(data=main_df, x='hum', y='cnt', label='Humidity', ax=ax4)
sns.scatterplot(data=main_df, x='windspeed', y='cnt', label='Windspeed', ax=ax4)

ax4.set_xlabel("Nilai Variabel Cuaca")
ax4.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig4)

st.divider()

st.subheader("Ringkasan Insight")

st.write("""
Penyewaan sepeda menunjukkan pola yang dinamis baik secara harian maupun per jam. 
Terlihat adanya peningkatan jumlah penyewaan pada periode tertentu serta pola penggunaan yang berbeda antara pengguna casual dan registered. 
Selain itu, faktor cuaca seperti suhu, kelembaban, dan kecepatan angin juga menunjukkan hubungan tertentu terhadap jumlah penyewaan, di mana beberapa variabel memiliki pengaruh yang lebih kuat dibandingkan yang lain.
""")