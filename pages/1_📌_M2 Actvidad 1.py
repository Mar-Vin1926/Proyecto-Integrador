import io
import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
from firebase_admin import credentials, initialize_app, firestore
import firebase_admin
import json
import toml

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


def descargar_excel(df, nombre_archivo):
    """Genera un archivo Excel a partir de un DataFrame y crea un botón de descarga."""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    st.download_button(
        label=f"Descargar {nombre_archivo}.xlsx",
        data=processed_data,
        file_name=f"{nombre_archivo}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

st.write("Datos de Libros")
descargar_excel(df_libros, "Libros")


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



def descargar_excel(df, nombre_archivo):
    """Genera un archivo Excel a partir de un DataFrame y crea un botón de descarga."""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    st.download_button(
        label=f"Descargar {nombre_archivo}.xlsx",
        data=processed_data,
        file_name=f"{nombre_archivo}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    st.write("Datos de Ciudades")
descargar_excel(df_ciudades, "Ciudades")


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

def descargar_excel(df, nombre_archivo):
    """Genera un archivo Excel a partir de un DataFrame y crea un botón de descarga."""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    st.download_button(
        label=f"Descargar {nombre_archivo}.xlsx",
        data=processed_data,
        file_name=f"{nombre_archivo}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
st.write("Datos de Inventario")
descargar_excel(df_productos, "Inventario")

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


def descargar_excel(df, nombre_archivo):
    """Genera un archivo Excel a partir de un DataFrame y crea un botón de descarga."""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    st.download_button(
        label=f"Descargar {nombre_archivo}.xlsx",
        data=processed_data,
        file_name=f"{nombre_archivo}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
st.write("Datos de Personas")
st.dataframe(df_personas)
descargar_excel(df_personas, "Personas")



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




st.header("DataFrame desde JSON")

df_json = pd.read_json("pages/data.json")
st.dataframe(df_json)

st.header("Solución")
code="""
Crea un archivo llamado data.json en la misma carpeta que tu script con el siguiente contenido:
    {"nombre": "Usuario1", "correo": "usuario1@example.com"},
    {"nombre": "Usuario2", "correo": "usuario2@example.com"},
    {"nombre": "Usuario3", "correo": "usuario3@example.com"}

df_json = pd.read_json("data.json")
st.dataframe(df_json)

"""
st.code(code, language='python')




st.header("DataFrame desde URL")

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"  # URL real de un archivo CSV
df_url = pd.read_csv(url)
st.dataframe(df_url)

st.header("Solución")
code="""
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"  # URL real de un archivo CSV
df_url = pd.read_csv(url)
st.dataframe(df_url)
"""
st.code(code, language='python')


def descargar_excel(df, nombre_archivo):
    """Genera un archivo Excel a partir de un DataFrame y crea un botón de descarga."""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    st.download_button(
        label=f"Descargar {nombre_archivo}.xlsx",
        data=processed_data,
        file_name=f"{nombre_archivo}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
st.write("Datos desde URL")
descargar_excel(df_url, "Datos_URL")





st.header("DataFrame desde SQLite")

conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes (nombre TEXT, calificacion INTEGER)")
cursor.execute("INSERT INTO estudiantes VALUES ('Ana', 90), ('Juan', 85), ('María', 95)")
conn.commit()

df_sqlite = pd.read_sql_query("SELECT * FROM estudiantes", conn)
st.dataframe(df_sqlite)

conn.close()

def descargar_excel(df, nombre_archivo):
    """Genera un archivo Excel a partir de un DataFrame y crea un botón de descarga."""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    st.download_button(
        label=f"Descargar {nombre_archivo}.xlsx",
        data=processed_data,
        file_name=f"{nombre_archivo}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )



st.write("Datos desde SQLite")
descargar_excel(df_sqlite, "Datos_SQLite")



st.header("Solución")
code="""
conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes (nombre TEXT, calificacion INTEGER)")
cursor.execute("INSERT INTO estudiantes VALUES ('Ana', 90), ('Juan', 85), ('María', 95)")
conn.commit()

df_sqlite = pd.read_sql_query("SELECT * FROM estudiantes", conn)
st.dataframe(df_sqlite)

conn.close()
"""
st.code(code, language='python')






st.header("DataFrame desde NumPy")

array_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_numpy = pd.DataFrame(array_np, columns=["Columna 1", "Columna 2", "Columna 3"])
st.dataframe(df_numpy)


def descargar_excel(df, nombre_archivo):
    """Genera un archivo Excel a partir de un DataFrame y crea un botón de descarga."""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    st.download_button(
        label=f"Descargar {nombre_archivo}.xlsx",
        data=processed_data,
        file_name=f"{nombre_archivo}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
st.write("Datos desde NumPy")
descargar_excel(df_numpy, "Datos_NumPy")



st.header("Solución")
code="""
st.header("DataFrame desde NumPy")

array_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_numpy = pd.DataFrame(array_np, columns=["Columna 1", "Columna 2", "Columna 3"])
st.dataframe(df_numpy)
"""
st.code(code, language='python')



st.header("FireBase")

def attrdict_to_dict(attrdict):
    """Convierte un objeto AttrDict a un diccionario Python estándar."""
    return dict(attrdict)

if not firebase_admin._apps:
    cred_toml = st.secrets["credentials"]
    cred_dict = toml.loads(toml.dumps(cred_toml))
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

# Inicializa el cliente de Firestore
db = firestore.client()

# Ejemplo: Lee datos de una colección llamada "usuarios"
usuarios_ref = db.collection("usuarios")
usuarios = usuarios_ref.stream()
data = []

# Muestra los datos en la aplicación Streamlit
st.title("Usuarios de Firestore")

for usuario in usuarios:
    usuario_dict = usuario.to_dict()
    usuario_dict["ID"] = usuario.id
    data.append(usuario_dict)

df_firebase = pd.DataFrame(data)
st.write("Datos desde Firebase")
st.dataframe(df_firebase)


# Ejemplo: Agregar datos a Firestore
st.header("Agregar Nuevo Usuario")

nombre_nuevo = st.text_input("Nombre:")
edad_nueva = st.number_input("Edad:", min_value=0, step=1)

if st.button("Agregar Usuario"):
    if nombre_nuevo and edad_nueva >= 0:
        nuevo_usuario = {"nombre": nombre_nuevo, "edad": edad_nueva}
        db.collection("usuarios").add(nuevo_usuario)
        st.success("Usuario agregado correctamente.")
    else:
        st.warning("Por favor, ingresa un nombre y una edad válida.")



st.header("Solución")

code="""
def attrdict_to_dict(attrdict):
   
    return dict(attrdict)

cred_toml = attrdict_to_dict(st.secrets["credentials"]) #<--- Modificacion
cred_dict = toml.loads(toml.dumps(cred_toml))
cred = credentials.Certificate(cred_dict)

# Inicializa la aplicación Firebase si aún no se ha inicializado
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Inicializa el cliente de Firestore
db = firestore.client()

# Ejemplo: Lee datos de una colección llamada "usuarios"
usuarios_ref = db.collection("usuarios")
usuarios = usuarios_ref.stream()

# Muestra los datos en la aplicación Streamlit
st.title("Usuarios de Firestore")

for usuario in usuarios:
    usuario_dict = usuario.to_dict()
    nombre = usuario_dict.get("nombre", "Nombre no disponible")
    edad = usuario_dict.get("edad", "Edad no disponible")
    st.write(f"ID: {usuario.id}, Nombre: {nombre}, Edad: {edad}")

# Ejemplo: Agregar datos a Firestore
st.header("Agregar Nuevo Usuario")

nombre_nuevo = st.text_input("Nombre:")
edad_nueva = st.number_input("Edad:", min_value=0, step=1)

if st.button("Agregar Usuario"):
    if nombre_nuevo and edad_nueva >= 0:
        nuevo_usuario = {"nombre": nombre_nuevo, "edad": edad_nueva}
        db.collection("usuarios").add(nuevo_usuario)
        st.success("Usuario agregado correctamente.")
    else:
        st.warning("Por favor, ingresa un nombre y una edad válida.")

"""
st.code(code, language="python")



