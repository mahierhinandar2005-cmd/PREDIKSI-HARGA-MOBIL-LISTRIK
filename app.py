import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

st.set_page_config(page_title="Prediksi Harga Mobil Listrik", page_icon="🚗")
st.title("🚗 Prediksi Harga Mobil Listrik Indonesia 2026")
st.markdown("Menggunakan **Artificial Neural Network (ANN)** - Project SC 2026")

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("model_ev.h5")
    scaler_X = joblib.load("scaler_X.pkl")
    scaler_y = joblib.load("scaler_y.pkl")
    return model, scaler_X, scaler_y

model, scaler_X, scaler_y = load_model()
st.success("✅ Model ANN berhasil dimuat!")

st.subheader("📝 Masukkan Spesifikasi Mobil")

col1, col2 = st.columns(2)

with col1:
    tahun = st.number_input("Tahun Mobil", 2020, 2026, 2026)
    baterai = st.number_input("Kapasitas Baterai (kWh)", 10.0, 150.0, 60.0)

with col2:
    jarak = st.number_input("Jarak Tempuh (km)", 100, 800, 400)
    daya = st.number_input("Tenaga (hp)", 30, 600, 150)

if st.button("💰 Prediksi Harga", type="primary"):
    input_data = np.array([[tahun, baterai, jarak, daya]])
    input_scaled = scaler_X.transform(input_data)
    pred_scaled = model.predict(input_data, verbose=0)
    harga = scaler_y.inverse_transform(pred_scaled)
    
    st.markdown("---")
    st.success(f"### 🎯 Estimasi Harga: **Rp {harga[0][0]:,.0f} Juta**")
    st.caption("Harga adalah OTR Jakarta dalam satuan Juta Rupiah")

st.markdown("---")
st.caption("Project SC 2026 - Prediksi Harga Mobil Listrik dengan ANN | Dataset 30+ Mobil Indonesia 2025-2026")import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

st.set_page_config(page_title="Prediksi Harga Mobil Listrik", page_icon="🚗")
st.title("🚗 Prediksi Harga Mobil Listrik Indonesia 2026")
st.markdown("Menggunakan **Artificial Neural Network (ANN)** - Project SC 2026")

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("model_ev.h5")
    scaler_X = joblib.load("scaler_X.pkl")
    scaler_y = joblib.load("scaler_y.pkl")
    return model, scaler_X, scaler_y

model, scaler_X, scaler_y = load_model()
st.success("✅ Model ANN berhasil dimuat!")

st.subheader("📝 Masukkan Spesifikasi Mobil")

col1, col2 = st.columns(2)

with col1:
    tahun = st.number_input("Tahun Mobil", 2020, 2026, 2026)
    baterai = st.number_input("Kapasitas Baterai (kWh)", 10.0, 150.0, 60.0)

with col2:
    jarak = st.number_input("Jarak Tempuh (km)", 100, 800, 400)
    daya = st.number_input("Tenaga (hp)", 30, 600, 150)

if st.button("💰 Prediksi Harga", type="primary"):
    input_data = np.array([[tahun, baterai, jarak, daya]])
    input_scaled = scaler_X.transform(input_data)
    pred_scaled = model.predict(input_data, verbose=0)
    harga = scaler_y.inverse_transform(pred_scaled)
    
    st.markdown("---")
    st.success(f"### 🎯 Estimasi Harga: **Rp {harga[0][0]:,.0f} Juta**")
    st.caption("Harga adalah OTR Jakarta dalam satuan Juta Rupiah")

st.markdown("---")
st.caption("Project SC 2026 - Prediksi Harga Mobil Listrik dengan ANN | Dataset 30+ Mobil Indonesia 2025-2026")
