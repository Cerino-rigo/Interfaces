import streamlit as st

# Definir funciones para las opciones del selectbox
def sensor_1():
    st.write("Seleccionaste el sensor 1 - Análisis de Tráfico en Tienda A")

def sensor_2():
    st.write("Seleccionaste el sensor 2 - Análisis de Tráfico en Tienda B")

def resumen():
    st.write("Seleccionaste Desplegar  - Resumen General de Tráfico")

# Sidebar con el selectbox
st.sidebar.title("Opciones de Análisis")
opcion_seleccionada = st.sidebar.selectbox("Selecciona una opción", ["Tienda A", "Tienda B", "Resumen General"])

# Mapeo de opciones a funciones
opciones_funciones = {
    "Tienda A": sensor_1,
    "Tienda B": sensor_2,
    "Resumen General": resumen
}

# Ejecutar la función correspondiente a la opción seleccionada
if opcion_seleccionada in opciones_funciones:
    opciones_funciones[opcion_seleccionada]()
