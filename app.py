import matplotlib.pyplot as plt
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
# se crea una casilla de verificación
build_scatter = st.checkbox('Construir un grafico de dispersión')
# if scat_button:  # al hacer clic en el botón
if build_scatter:
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispesión para el conjunto de datos de anuncios de venta de coches, precio vs kilometraje')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# vamos a hacer un grafico dinamico con los modelos 3 modelos mas repetidos en la DB
# Agregar un subtitulo o texto informativo
st.subheader('Variación de precio con respecto al kilometraje')

# Agregar un botón para elegir el modelo
selected_model = st.radio('Selecciona un modelo:',  [
                          'ford f-150', 'chevrolet silverado 1500', 'ram 1500'])

# Filtrar los datos según el modelo seleccionado
filtered_df = car_data[car_data['model'] == selected_model]

# Verificar el modelo seleccionado y generar el gráfico correspondiente
if selected_model == 'ford f-150':  # codigo para el modelo ford f-150
    fig, ax = plt.subplots()
    ax.scatter(filtered_df['odometer'], filtered_df['price'], color='red')
    ax.set_xlabel('Kilometraje')
    ax.set_ylabel('Precio USD')
    ax.set_title(f'Variación de precio vs. kilometraje para {selected_model}')
    st.pyplot(fig)
elif selected_model == 'chevrolet silverado 1500':  # codigo para el modelo chevrolet silverado
    fig, ax = plt.subplots()
    ax.scatter(filtered_df['odometer'], filtered_df['price'], color='grey')
    ax.set_xlabel('Kilometraje')
    ax.set_ylabel('Precio USD')
    ax.set_title(f'Variación de precio vs. kilometraje para {selected_model}')
    st.pyplot(fig)
    pass
elif selected_model == 'ram 1500':  # Código para el gráfico de Ram 1500

    fig, ax = plt.subplots()
    ax.scatter(filtered_df['odometer'], filtered_df['price'], color='black')
    ax.set_xlabel('Kilometraje')
    ax.set_ylabel('Precio USD')
    ax.set_title(f'Variación de precio vs. kilometraje para {selected_model}')
    st.pyplot(fig)
    pass
