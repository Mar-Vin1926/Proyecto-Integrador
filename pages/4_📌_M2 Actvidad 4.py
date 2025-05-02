import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")


# Ejemplo de DataFrame.

data = {
    'Titulo': ['El Padrino', 'Interestelar', 'Parasite','Mad Max: Fury Road', 'Your Name'],
    'Año': [1972, 2014, 2019, 2015, 2016],
        'Género': ['Crimen', 'Ciencia Ficción', 'Drama', 'Acción', 'Animación'],
        'Puntuación IMDb': [9.2, 8.6, 8.6, 8.5, 8.4]}
df = pd.DataFrame(data)


st.title('Explorador de Películas')
st.subheader('Utilizando .loc e .iloc con streamlit')



# Mostrar el DataFrame completo
st.subheader('DataFrame Completo')
st.dataframe(df)

st.markdown('---')

# Seleccion por índice con . iloc
st.subheader('Seleccionar por índice con (.iloc)')
indice_seleccionado = st.number_input('Ingrese el índice de la fila que desea seleccionar:', min_value=0, max_value=len(df)-1, value=0)
if st.button('Mostrar fila por idice'):
    try:
        fila_iloc = df.iloc[[indice_seleccionado]]
        st.write('Dila seleccionada (usando .iloc)')
        st.dataframe(fila_iloc)
    except IndexError:
        st.error('Índice fuera de rango. Por favor, ingrese un índice válido.')

st.markdown('---')

# Filtrado por condición con .loc 
st.subheader('Filtrado por condición (.loc)')
columna_filtro = st.selectbox('Seleccione la columna para filtrar:', df.columns)
valor_filtro = st.text_input(f'Ingrese el valor para filtrar en la columna {columna_filtro}:')
if st.button('Filtrar por valor'):
    if valor_filtro:
        try:
            fila_loc = df.loc[df[columna_filtro] == valor_filtro]
            st.write(f'Filas donde "{columna_filtro}" es igual a "{valor_filtro}" (usando .loc):')
            st.dataframe(fila_loc)
        except KeyError:
            st.error(f'La columna "{columna_filtro}" no existe.')
    else:
        st.warning('Por favor, ingrese un valor para filtrar.')

st.markdown('---')

# Selección de columnas
st.subheader('Seleccionar columnas')
columnas_seleccionadas = st.multiselect('Seleccione las columnas que desea ver:', df.columns.tolist(), default=df.columns.tolist())
if columnas_seleccionadas:
    st.write('Columnas seleccionadas:')
    st.dataframe(df[columnas_seleccionadas])
else:
    st.info('Seleccione al menos una columna.')

st.markdown('---')

# Modificacion de una celda con .loc
st.subheader('Modificar una celda con (.loc)')
indice_modificar = st.number_input('Ingrese el indice de la fila que desea modificar:', min_value=0, max_value=len(df)-1, value=0)
columna_modificar = st.selectbox('Seleccione la columna que desea modificar:', df.columns, key='columna_modificar')
nuevo_valor = st.text_input('Ingrese el nuevo valor:', key='nuevo_valor')
if st.button('Modficar Celdar'):
    try:
        df_modificado = df.copy() # Importante crear una copia para no modificar el original
        df.modificado.loc[indcie_modificar, columna_modificar] = nuevo_valor
        st.dataframe(df_modificado)
    except KeyError:
        st.error('Inice o columna invalida.')
    
st.markdown('---')

st.header("Solución")
code="""
# Ejemplo de DataFrame.

data = {
    'Titulo': ['El Padrino', 'Interestelar', 'Parasite','Mad Max: Fury Road', 'Your Name'],
    'Año': [1972, 2014, 2019, 2015, 2016],
        'Género': ['Crimen', 'Ciencia Ficción', 'Drama', 'Acción', 'Animación'],
        'Puntuación IMDb': [9.2, 8.6, 8.6, 8.5, 8.4]}
df = pd.DataFrame(data)


st.title('Explorador de Películas')
st.subheader('Utilizando .loc e .iloc con streamlit')



# Mostrar el DataFrame completo
st.subheader('DataFrame Completo')
st.dataframe(df)

st.markdown('---')

# Seleccion por índice con . iloc
st.subheader('Seleccionar por índice con (.iloc)')
indice_seleccionado = st.number_input('Ingrese el índice de la fila que desea seleccionar:', min_value=0, max_value=len(df)-1, value=0)
if st.button('Mostrar fila por idice'):
    try:
        fila_iloc = df.iloc[[indice_seleccionado]]
        st.write('Dila seleccionada (usando .iloc)')
        st.dataframe(fila_iloc)
    except IndexError:
        st.error('Índice fuera de rango. Por favor, ingrese un índice válido.')

st.markdown('---')

# Filtrado por condicion con .loc 
st.subheader('Filtrado por condición (.loc)')
columna_filtro = st.selectbox('Seleccione la columna para filtrar:', df.columns)
valor_filtro = st.text_input(f'Ingrese el valor para filtrar en la columna {columna_filtro}:')
if st.button('Filtrar por valor'):
    if valor_filtro:
        try:
            fila_loc = df.loc[df[columna_filtro] == valor_filtro]
            st.write(f'Filas donde "{columna_filtro}" es igual a "{valor_filtro}" (usando .loc):')
            st.dataframe(fila_loc)
        except KeyError:
            st.error(f'La columna "{columna_filtro}" no existe.')
    else:
        st.warning('Por favor, ingrese un valor para filtrar.')

st.markdown('---')

# Selección de columnas
st.subheader('Seleccionar columnas')
columnas_seleccionadas = st.multiselect('Seleccione las columnas que desea ver:', df.columns.tolist(), default=df.columns.tolist())
if columnas_seleccionadas:
    st.write('Columnas seleccionadas:')
    st.dataframe(df[columnas_seleccionadas])
else:
    st.info('Seleccione al menos una columna.')

st.markdown('---')

# Modificacion de una celda con .loc
st.subheader('Modificar una celda con (.loc)')
indice_modificar = st.number_input('Ingrese el indice de la fila que desea modificar:', min_value=0, max_value=len(df)-1, value=0)
columna_modificar = st.selectbox('Seleccione la columna que desea modificar:', df.columns, key='columna_modificar')
nuevo_valor = st.text_input('Ingrese el nuevo valor:', key='nuevo_valor')
if st.button('Modficar Celdar'):
    try:
        df_modificado = df.copy() # Importante crear una copia para no modificar el original
        df.modificado.loc[indcie_modificar, columna_modificar] = nuevo_valor
        st.dataframe(df_modificado)
    except KeyError:
        st.error('Inice o columna invalida.')
    
st.markdown('---')
"""
st.code(code, language='python')

