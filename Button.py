import streamlit as st
import pandas as pd
import numpy as np

# Funciones de análisis para cada tienda
def analisis_tienda_a(tienda_df):
    st.write("Análisis para la Tienda A")
    st.write(tienda_df.head())

def analisis_tienda_b(tienda_df):
    st.write("Análisis para la Tienda B")
    st.write(tienda_df.head())

def analisis_tienda_c(tienda_df):
    st.write("Análisis para la Tienda C")
    st.write(tienda_df.head())

# Sidebar
st.sidebar.title("Configuración")
sensor_seleccionado = st.sidebar.radio(":convenience_store: Seleccionar sensor", ["Sensor A", "Sensor B", "Sensor C"])

tipo_grafico = st.sidebar.selectbox(":bar_chart: Seleccionar Tipo de Gráfico", ["Gráfico de Barras", "Gráfico de Líneas", "Scatter Plot"])

# Datos de ejemplo
data = {
    'Sensor A': np.random.randint(1, 100, 100),
    'Sensor B': np.random.randint(1, 100, 100),
    'Sensor C': np.random.randint(1, 100, 100)
}
df = pd.DataFrame(data)

if 'button' not in st.session_state:
        st.session_state.button = False

def click_button():
        st.session_state.button = not st.session_state.button

# Botones en la parte superior
col1, col2, col3 = st.columns(3)
if col1.button(":department_store: **Tienda A**", help="Haz clic para ver análisis de Tienda A", use_container_width=True):
    analisis_tienda_a(df["Sensor A"])

if col2.button(":factory: $\t Tienda B$", help="Haz clic para ver análisis de Tienda B", use_container_width=True):
    analisis_tienda_b(df["Sensor B"])


if col3.button(":hospital: Tienda C", help="Haz clic para ver análisis de Tienda C", use_container_width=True, on_click=click_button):
    if st.session_state.button:
        analisis_tienda_c(df["Sensor C"])

    
# Línea divisoria visual
st.markdown('---')
st.markdown('<hr style="border: 2px solid #CB1A2D; background-color: #3498db; height: 5px;">', unsafe_allow_html=True)
    

# Agregar gráfico según la selección
if tipo_grafico == "Gráfico de Barras":
    st.bar_chart(df[sensor_seleccionado])
elif tipo_grafico == "Gráfico de Líneas":
    st.line_chart(df[sensor_seleccionado])
elif tipo_grafico == "Scatter Plot":
    st.scatter_chart(df[sensor_seleccionado])
