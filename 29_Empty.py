import streamlit as st
import time

# Crear un espacio reservado con st.empty()
placeholder = st.empty()

# Botón en el sidebar para actualizar el contenido del espacio reservado
if st.sidebar.button("Actualizar Contenido"):
    with placeholder:
        st.write("Actualizando contenido...")
        # Simulación de una tarea que lleva tiempo
        time.sleep(5)
        st.write("¡Contenido actualizado!")

# Agregar contenido fuera del espacio reservado
st.write("Este contenido está fuera del espacio reservado.")
