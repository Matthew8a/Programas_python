import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")

st.header("Proyecto 7")

check_hist = st.checkbox("Genera un histograma")

if check_hist:
  st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
  histo = px.histogram(car_data, x="odometer")
  st.plotly_chart(fig, use_container_width=True)

check_disp = st.checkbox("Genera un gráfico de dispersión")

if check_disp:
  st.write("Creacion de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches")
  disp = px.scatter(car_data)
