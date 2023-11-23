import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

# Crear un DataFrame de ejemplo
data = {
    'Fecha': pd.date_range('2023-01-01', '2023-01-10'),
    'Valor_A': np.random.randint(10, 50, 10),
    'Valor_B': np.random.randint(20, 60, 10)
}
df = pd.DataFrame(data)

# Título de la aplicación
st.title('Dashboard de Análisis de Datos')

# Crear contenedor para el gráfico
with st.container():
    # Seleccionar tipo de gráfico
    chart_type = st.selectbox('Seleccionar tipo de gráfico', ['Línea', 'Barra'])

    # Crear gráfico según la selección
    if chart_type == 'Línea':
        fig = px.line(df, x='Fecha', y=['Valor_A', 'Valor_B'], title='Gráfico de Línea')
    elif chart_type == 'Barra':
        fig = px.bar(df, x='Fecha', y=['Valor_A', 'Valor_B'], title='Gráfico de Barras')

    # Desplegar el gráfico
    st.plotly_chart(fig)

# Agregar más elementos al dashboard fuera del contenedor
st.subheader('Resumen de Datos')
st.dataframe(df.describe())

# Agregar otro contenedor para información adicional
with st.container():
    st.subheader('Información Adicional')
    st.write('Este es un contenedor adicional con información relevante.')

# Otros elementos visuales, como botones, sliders, etc.
st.sidebar.header('Configuración')
selected_option = st.sidebar.selectbox('Seleccionar opción', ['Opción 1', 'Opción 2', 'Opción 3'])
st.sidebar.write(f'Opción seleccionada: {selected_option}')

