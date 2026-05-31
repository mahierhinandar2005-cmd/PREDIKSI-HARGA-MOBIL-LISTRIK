import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import pickle

st.set_page_config(page_title="Prediksi Harga Mobil", page_icon="🚗")
st.title("🚗 Prediksi Harga Mobil Listrik Indonesia 2026")

# Dataset (built-in di app)
data = pd.DataFrame({
    'Baterai_kWh': [60.5, 82.5, 26.7, 31.0, 77.4, 77.4, 78.0, 78.0],
    'Range_km': [480, 650, 300, 333, 550, 610, 629, 533],
    'Harga_Juta': [515, 750, 190, 258, 785, 1090, 1290, 1690]
})

# Training model langsung di app
X = data[['Baterai_kWh', 'Range_km']]
y = data['Harga_Juta']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

st.success("✅ Model siap!")

st.subheader("Masukkan Spesifikasi Mobil")

col1, col2 = st.columns(2)

with col1:
    baterai = st.number_input("Baterai (kWh)", 20.0, 150.0, 60.0)

with col2:
    jarak = st.number_input("Range (km)", 100, 800, 400)

if st.button("Prediksi Harga"):
    pred = model.predict([[baterai, jarak]])
    st.success(f"💰 Estimasi Harga: Rp {pred[0]:,.0f} Juta")

st.caption("Project SC 2026 - Prediksi Harga Mobil Listrik")
