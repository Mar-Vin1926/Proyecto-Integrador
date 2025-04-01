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
code="""
st.header("DataFrame desde Diccionario")

libros = {
    "título": ["Cien años de soledad", "1984", "El señor de los anillos", "Orgullo y prejuicio"],
   "autor": ["Gabriel García Márquez", "George Orwell", "J.R.R. Tolkien", "Jane Austen"],
    "año de publicación": [1967, 1949, 1954, 1813],
    "género": ["Realismo mágico", "Ciencia ficción", "Fantasía", "Romance"]}"


df_libros = pd.DataFrame(libros)
st.dataframe(df_libros)"
"""
st.code(code, language='python')


st.header("DataFrame desde Lista de Diccionarios")

ciudades = [
    {"nombre": "Tokio", "población": 13929286, "país": "Japón"},
    {"nombre": "Delhi", "población": 11007835, "país": "India"},
    {"nombre": "Shanghái", "población": 26317104, "país": "China"},
    {"nombre": "Ciudad de México", "población": 8851080, "país": "México"}
]

df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)

st.header("Solución")
code="""

ciudades = [
    {"nombre": "Tokio", "población": 13929286, "país": "Japón"},
    {"nombre": "Delhi", "población": 11007835, "país": "India"},
    {"nombre": "Shanghái", "población": 26317104, "país": "China"},
    {"nombre": "Ciudad de México", "población": 8851080, "país": "México"}
]

df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)
"""
st.code(code, language='python')



st.header("DataFrame desde Lista de Listas")

productos = [
    ["Laptop", 1200, 10],
    ["Smartphone", 800, 20],
    ["Tablet", 300, 15],
    ["Auriculares", 100, 50]
]

df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)

st.header("Solución")
code="""
productos = [
    ["Laptop", 1200, 10],
    ["Smartphone", 800, 20],
    ["Tablet", 300, 15],
    ["Auriculares", 100, 50]
]

df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)
"""
st.code(code, language='python')


st.header("DataFrame desde Series")

nombres = pd.Series(["Paola", "Marvin", "Kevin", "Pedro"])
edades = pd.Series([18, 32, 32, 35])
ciudades = pd.Series(["Bello", "Envigado", "La guajira", "Sevilla"])

df_personas = pd.DataFrame({"Nombre": nombres, "Edad": edades, "Ciudad": ciudades})
st.dataframe(df_personas)

st.header("Solución")
code="""
nombres = pd.Series(["Paola", "Marvin", "Kevin", "Pedro"])
edades = pd.Series([18, 32, 32, 35])
ciudades = pd.Series(["Bello", "Envigado", "La guajira", "Sevilla"])

df_personas = pd.DataFrame({"Nombre": nombres, "Edad": edades, "Ciudad": ciudades})
st.dataframe(df_personas)
"""
st.code(code, language='python')





st.header("DataFrame desde CSV")

df_csv = pd.read_csv("pages/data.csv", sep= ";")
st.dataframe(df_csv)


st.header("Solución")
code="""
"Se crea un archivo con el nombre data.csv y se pone en la carpeta raiz de los archivos .py que estas manipulando
"
df_csv = pd.read_csv("pages/data.csv")
st.dataframe(df_csv)
"""
st.code(code, language='python')




st.header("DataFrame desde Excel")

df_excel = pd.read_excel("pages/data.xlsx")
st.dataframe(df_excel)

st.header("Solución")
code="""
se instala, la libreria para manipular excel "openpyxl" con pip install openpyxl.
Se crea el archivo data.xlsx y se llama con df.excel = pd.read_excel("RUTA DONDE TIENES EL ARCHIVO")

df_excel = pd.read_excel("data.xlsx")
st.dataframe(df_excel)
"""
st.code(code, language='python')