import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("tabular_data_general1.xlsx", index_col=0)

from datetime import datetime, date, time
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

df['Day'] = df['timestamp'].dt.day_name()

st.title('Análisis de datos tabulares')
st.dataframe(df)

st.subheader('Gráfico de líneas')
fig, ax = plt.subplots()
df[['Day', 'total_visits']].groupby(df['Day']).sum().plot(ax=ax, title = 'Visitas por día')
st.pyplot(fig)