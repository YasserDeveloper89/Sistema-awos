import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="AeroWeather App", layout="wide")

st.title("🌤️ AeroWeather App - Sistema AWOS/ATI en tiempo real")

# Función para simular datos AWOS
def generate_awos_data():
    now = datetime.utcnow()
    return {
        "Hora UTC": now.strftime("%H:%M:%S"),
        "Temperatura (°C)": round(np.random.uniform(15, 30), 1),
        "Humedad (%)": round(np.random.uniform(40, 90), 1),
        "Presión (hPa)": round(np.random.uniform(1000, 1020), 1),
        "Viento (km/h)": round(np.random.uniform(5, 25), 1),
        "Dirección del Viento (°)": round(np.random.uniform(0, 360), 1),
        "Visibilidad (km)": round(np.random.uniform(5, 10), 1),
        "Altura de Nube (pies)": int(np.random.uniform(1000, 5000)),
        "Condición del Cielo": np.random.choice(["Despejado", "Nublado", "Lluvia Ligera", "Neblina"])
    }

# Función para generar mensaje ATIS
def generar_atis(data):
    return f"""
Información ATIS Simulada:
Hora: {data['Hora UTC']} UTC
Viento: {data['Dirección del Viento (°)']}° a {data['Viento (km/h)']} km/h
Visibilidad: {data['Visibilidad (km)']} km
Condición: {data['Condición del Cielo']}
Temperatura: {data['Temperatura (°C)']} °C
Humedad: {data['Humedad (%)']}%
Presión: {data['Presión (hPa)']} hPa
Altura de Nube: {data['Altura de Nube (pies)']} pies
""".strip()

# Mostrar datos AWOS
st.subheader("📡 Datos Meteorológicos de Estación AWOS")
awos_data = generate_awos_data()
df = pd.DataFrame([awos_data])

# ✅ Muestra sin estilos ni errores
st.dataframe(df, use_container_width=True)

# Mostrar mensaje ATIS
st.subheader("🛫 Mensaje ATIS Generado")
atis = generar_atis(awos_data)
st.code(atis)

# Pie de página
