import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV del conjunto de datos
car_data = pd.read_csv('./vehicles_us.csv')

# Crear el contenido de la aplicación Streamlit
# Encabezado
st.header('Análisis de Datos de Vehículos en Venta')

# Crear casillas de verificación
show_hist = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

# Mostrar el histograma si la casilla está seleccionada
if show_hist:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Mostrar el gráfico de dispersión si la casilla está seleccionada
if show_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
