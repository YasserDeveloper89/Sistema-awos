import streamlit as st
import pandas as pd
import numpy as np
import datetime
import random

st.set_page_config(page_title="AeroWeather App - Sistema AWOS", page_icon="🌤️", layout="centered")

st.markdown("# 🌀 AeroWeather - Sistema AWOS/ATI con alertas en tiempo real")
st.markdown("## 📈 Datos Meteorológicos de estaciones AWOS/ATI")

# ------------------ Funciones ------------------

def generar_datos_awos():
    return {
        "Hora UTC": datetime.datetime.utcnow().strftime("%H:%M:%S"),
        "Temperatura (°C)": round(random.uniform(-5, 40), 1),
        "Humedad (%)": random.randint(10, 100),
        "Presión (hPa)": round(random.uniform(980, 1030), 1),
        "Visibilidad (m)": random.randint(50, 10000),
        "Velocidad Viento (kt)": random.randint(0, 40),
        "Dirección Viento (°)": random.choice([0, 45, 90, 135, 180, 225, 270, 315])
    }

def generar_dataframe(filas=10):
    data = [generar_datos_awos() for _ in range(filas)]
    return pd.DataFrame(data)

def detectar_alertas(df):
    alertas = []
    for index, row in df.iterrows():
        if row["Visibilidad (m)"] < 800:
            alertas.append((index, "🌫️ Baja visibilidad (<800 m)"))
        if row["Velocidad Viento (kt)"] > 30:
            alertas.append((index, "🌪️ Viento fuerte (>30 kt)"))
        if row["Presión (hPa)"] < 985:
            alertas.append((index, "🌧️ Presión atmosférica baja"))
        if row["Temperatura (°C)"] < -3 or row["Temperatura (°C)"] > 38:
            alertas.append((index, "🔥 Temperatura extrema"))

    return alertas

def mostrar_alertas(alertas, df):
    if alertas:
        st.warning("⚠️ **Alertas Meteorológicas Detectadas**:")
        for idx, mensaje in alertas:
            st.markdown(f"- 🔎 {df['Hora UTC'][idx]} — {mensaje}")
    else:
        st.success("✅ Condiciones meteorológicas estables en todas las estaciones simuladas.")

# ------------------ UI Principal ------------------

df = generar_dataframe()
st.dataframe(df)

alertas = detectar_alertas(df)
mostrar_alertas(alertas, df)

# Pie de página
st.markdown("---")
st.caption("Sistema simulado para demostración técnica | Desarrollado con ❤️ en Streamlit")
