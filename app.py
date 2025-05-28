
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="ADR AeroWeather", layout="wide")

st.title("🌤️ ADR AeroWeather - Sistema AWOS Simulado")

# Simulación de datos
def generate_awos_data():
    now = datetime.utcnow()
    data = {
        "Hora UTC": now.strftime("%H:%M:%S"),
        "Temperatura (°C)": round(np.random.uniform(15, 30), 1),
        "Humedad (%)": round(np.random.uniform(40, 90), 1),
        "Presión (hPa)": round(np.random.uniform(1000, 1020), 1),
        "Viento (km/h)": round(np.random.uniform(5, 25), 1),
        "Dirección del Viento (°)": round(np.random.uniform(0, 360), 1),
        "Visibilidad (km)": round(np.random.uniform(5, 10), 1),
        "Altura de Nube (pies)": round(np.random.uniform(1000, 5000)),
        "Condición del Cielo": np.random.choice(["Despejado", "Nublado", "Lluvia Ligera", "Neblina"])
    }
    return data

# Función para generar mensaje ATIS
def generar_atis(data):
    mensaje = f"""
Información ATIS Simulada:
Hora: {data['Hora UTC']} UTC
Viento: {data['Dirección del Viento (°)']}° a {data['Viento (km/h)']} km/h
Visibilidad: {data['Visibilidad (km)']} km
Condición: {data['Condición del Cielo']}
Temperatura: {data['Temperatura (°C)']} °C, Humedad: {data['Humedad (%)']}%
Presión: {data['Presión (hPa)']} hPa
Altura de Nube: {data['Altura de Nube (pies)']} pies
"""
    return mensaje.strip()

# Mostrar datos simulados
st.subheader("📡 Datos Meteorológicos de Estación AWOS")
awos_data = generate_awos_data()
df = pd.DataFrame([awos_data])
st.dataframe(df.style.highlight_max(axis=1))

# Mostrar mensaje ATIS
st.subheader("🛫 Mensaje ATIS Generado")
atis_msg = generar_atis(awos_data)
st.code(atis_msg, language="markdown")

# Nota final
st.info("Esta es una simulación profesional del sistema AWOS/ATIS basada en las soluciones de ADR Technology S.A.C.")
