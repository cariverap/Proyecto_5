import streamlit as st
import pandas as pd
import plotly.express as px

# para la app este es el encabezado o título
st.header('Anuncios de venta de Automóviles')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

build_histogram = st.checkbox('Construir un histograma')  # crear una casilla
# se creara un histograma que distribuya la cantidad de kilometraje que poseen los autos

if build_histogram:
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Se construye un grafico de dispersión de la variacion de los precios de automoviles en función del kilometraje

# se creauna casilla de verificación
build_scatter = st.checkbox('Construir un grafico de dispersión')
# if scat_button:  # al hacer clic en el botón
if build_scatter:
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispesión para el conjunto de datos de anuncios de venta de coches, precio vs kilometraje')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price", color='petal_length')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# build_histogram = st.checkbox('Construir un histograma')

# if build_histogram: # si la casilla de verificación está seleccionada
#    st.write('Construir un histograma para la columna odómetro')
    ...
