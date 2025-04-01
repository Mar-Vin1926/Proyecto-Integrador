import streamlit as st
import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
import json
import requests

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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



st.header("DataFrame desde Diccionario")

libros = {
    "título": ["Cien años de soledad", "1984", "El señor de los anillos", "Orgullo y prejuicio"],
    "autor": ["Gabriel García Márquez", "George Orwell", "J.R.R. Tolkien", "Jane Austen"],
    "año de publicación": [1967, 1949, 1954, 1813],
    "género": ["Realismo mágico", "Ciencia ficción", "Fantasía", "Romance"]
}

df_libros = pd.DataFrame(libros)
st.dataframe(df_libros)


st.header("Solución")

