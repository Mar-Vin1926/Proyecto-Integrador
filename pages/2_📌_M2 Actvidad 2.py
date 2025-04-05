import streamlit as st
import pandas as pd
import io

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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



# --- 1. Cargar el dataset ---
# Aquí le decimos a Pandas que lea el archivo "estudiantes_colombia.csv".
# Imagina que Pandas abre la tabla de Excel que tenemos.
df = pd.read_csv("static/datasets/estudiantes_colombia.csv")
st.dataframe(df)

st.header("Solución")
code="""
# --- 1. Cargar el dataset ---
# Aquí le decimos a Pandas que lea el archivo "estudiantes_colombia.csv".
# Imagina que Pandas abre la tabla de Excel que tenemos.
df = pd.read_csv("static/datasets/estudiantes_colombia.csv")
st.dataframe(df)
"""
st.code(code, language='python')


# ---2. Mostrar las primeras 5 filas ---
st.subheader("Primeras 5 filas del dataset")
st.dataframe(df.head())

st.header("Solución")
code="""
st.subheader("Primeras 5 filas del dataset")
st.dataframe(df.head())
"""
st.code(code , language='python')

# ---3. Mostrar las ultimas 5 filas ---
st.subheader("Las ultimas 5 filas del dataset")
st.dataframe(df.tail())

st.header("Solución")
code="""
st.subheader("Primeras 5 filas del dataset")
st.dataframe(df.head())
"""
st.code(code, language='python')

# ---4. Mostrar informacion del dataset
buffer = io.StringIO()
df.info(buf=buffer)
info_string = buffer.getvalue()

st.write("Información del dataset:")
st.text(info_string)

st.header("Solución")
code="""
buffer = io.StringIO()
df.info(buf=buffer)
info_string = buffer.getvalue()

st.write("Información del dataset:")
st.text(info_string)
"""
st.code(code, language='python')


# ---5. La función .describe() de Pandas nos da estadísticas descriptivas de las
# columnas numéricas, como la media, la desviación estándar, los valores mínimo y máximo, etc.
st.write("Estadísticas descriptivas:")
st.dataframe(df.describe())

# --- 6. Seleccionar columnas para mostrar ---
st.subheader("Seleccionar columnas para mostrar")
# Obtenemos la lista de todas las columnas de todo el datset.
columnas= df.columns.to_list()

# Usamos un widget de Streamlit llamado multiselect para que el usuario pueda
# elegir qué columnas quiere ver.

columnas_seleccionadas = st.multiselect("Seleccionamos las columnas que queremos ver:", columnas, default=["nombre", "edad", "promedio"])

# Si el usuario selecciona alguna columna, las mostramos.
if columnas_seleccionadas:
    st.write("Columnas seleccionadas:")
    st.dataframe(df[columnas_seleccionadas])
else:
    st.info("Por favor seleccionar almenos una columna para mostrar.")

st.header("Solución")
code="""
# ---5. La función .describe() de Pandas nos da estadísticas descriptivas de las
# columnas numéricas, como la media, la desviación estándar, los valores mínimo y máximo, etc.
st.write("Estadísticas descriptivas:")
st.dataframe(df.describe())

# --- 6. Seleccionar columnas para mostrar ---
st.subheader("Seleccionar columnas para mostrar")
# Obtenemos la lista de todas las columnas de todo el datset.
columnas= df.columns.to_list()

# Usamos un widget de Streamlit llamado multiselect para que el usuario pueda
# elegir qué columnas quiere ver.

columnas_seleccionadas = st.multiselect("Seleccionamos las columnas que queremos ver:", columnas, default=["nombre", "edad", "promedio"])

# Si el usuario selecciona alguna columna, las mostramos.
if columnas_seleccionadas:
    st.write("Columnas seleccionadas:")
    st.dataframe(df[columnas_seleccionadas])
else:
    st.info("Por favor seleccionar almenos una columna para mostrar.")
"""
st.code(code, language='python')

# --- 7. Filtrar estudiantes por promedio ---
st.subheader("Filtrar estudiantes por promedio")

# Encontramos el promedio maximo para establecer el rango del slider.
max_promedio = float(df['promedio'].max())

# Creamos un slider (una barra deslizante) para que el usuario pueda elegir
# el valor mínimo de promedio que quiere ver.

promedio_minimo = st.slider("Mostrar estudiantes co promedio mayor o igual a:", 0.0, max_promedio, 3.0)

# Filtramos el dataset para mostrar solo los estudiantes con un promedio mayor o igual al valor del slider.
estudiantes_filtrados = df[df['promedio'] >= promedio_minimo]

# Mostramos lo estudiantes filtrados.
st.write(f"Estudiantes con promedio mayor o igual a {promedio_minimo}:")
st.dataframe(estudiantes_filtrados)

st.header("Solución")
code="""
# --- 7. Filtrar estudiantes por promedio ---
st.subheader("Filtrar estudiantes por promedio")

# Encontramos el promedio maximo para establecer el rango del slider.
max_promedio = float(df['promedio'].max())

# Creamos un slider (una barra deslizante) para que el usuario pueda elegir
# el valor mínimo de promedio que quiere ver.

promedio_minimo = st.slider("Mostrar estudiantes co promedio mayor o igual a:", 0.0, max_promedio, 3.0)

# Filtramos el dataset para mostrar solo los estudiantes con un promedio mayor o igual al valor del slider.
estudiantes_filtrados = df[df['promedio'] >= promedio_minimo]

# Mostramos lo estudiantes filtrados.
st.write(f"Estudiantes con promedio mayor o igual a {promedio_minimo}:")
st.dataframe(estudiantes_filtrados)

"""
st.code(code, language='python')