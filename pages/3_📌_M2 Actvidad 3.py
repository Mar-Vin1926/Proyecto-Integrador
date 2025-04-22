import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker
import random

# Configuración de la página
st.set_page_config(
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3: Filtros Dinámicos")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad permite explorar el filtrado dinámico de datos utilizando Pandas y Streamlit.
Los filtros en la barra lateral se pueden activar para modificar el DataFrame mostrado.
""")

st.header("Objetivos de aprendizaje")
st.markdown("""
- Aplicar técnicas de filtrado de Pandas en una aplicación interactiva.
- Utilizar widgets de Streamlit para crear controles de filtrado dinámicos.
- Construir una interfaz de usuario intuitiva para la exploración de datos.
""")

# --- Enlace a Google Colab (Opcional) ---
st.header("Enlace a Google Colab")
colab_url = "https://colab.research.google.com/drive/1BfOHf4ic4jhgZK-Rq3zKuZgBDPLjapmr?authuser=0#scrollTo=OZzcBodmZz90"
st.markdown(f"[Abrir proyecto en Google Colab]({colab_url})", unsafe_allow_html=True)

st.header("Solución")

# --- Generación del DataFrame ---
fake = Faker('es_CO')
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)
n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',  # Caribe
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',  # Andina
            'Cali', 'Quibdó', 'Buenaventura',           # Pacífica
            'Villavicencio', 'Yopal',                    # Orinoquía
            'Leticia', 'Puerto Inírida'                  # Amazonía
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)}
df_nuevo = pd.DataFrame(data)
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])

# --- Barra lateral para los filtros ---
st.sidebar.header("Filtros Dinámicos")
df_filtrado = df_nuevo.copy() # Inicializamos con el DataFrame original

# 1. Filtro por rango de edad
filtrar_edad = st.sidebar.checkbox("Filtrar por rango de edad")
if filtrar_edad:
    min_edad, max_edad = st.sidebar.slider("Seleccione el rango de edad", 15, 75, (15, 75))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

# 2. Filtro por municipios específicos
filtrar_municipio = st.sidebar.checkbox("Filtrar por municipios")
municipios_opciones = ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida']
if filtrar_municipio:
    municipios_seleccionados = st.sidebar.multiselect("Seleccione los municipios", municipios_opciones)
    if municipios_seleccionados:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(municipios_seleccionados)]

# 3. Filtro por ingreso mensual mínimo
filtrar_ingreso_minimo = st.sidebar.checkbox("Filtrar por ingreso mensual mínimo")
if filtrar_ingreso_minimo:
    ingreso_minimo = st.sidebar.slider("Ingrese el ingreso mensual mínimo", 800000, 12000000, 800000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_minimo]

# 4. Filtro por ocupación
filtrar_ocupacion = st.sidebar.checkbox("Filtrar por ocupación")
ocupaciones_opciones = ['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico', 'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero']
if filtrar_ocupacion:
    ocupaciones_seleccionadas = st.sidebar.multiselect("Seleccione las ocupaciones", ocupaciones_opciones)
    if ocupaciones_seleccionadas:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(ocupaciones_seleccionadas)]

# 5. Filtro por tipo de vivienda no propia
filtrar_no_propia = st.sidebar.checkbox("Filtrar personas sin vivienda propia")
if filtrar_no_propia:
    df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

# 6. Filtro por nombres que contienen una cadena
filtrar_nombre = st.sidebar.checkbox("Filtrar por nombre")
if filtrar_nombre:
    texto_nombre = st.sidebar.text_input("Ingrese texto a buscar en el nombre")
    if texto_nombre:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto_nombre, case=False, na=False)]

# 7. Filtro por año de nacimiento específico
filtrar_año_nacimiento = st.sidebar.checkbox("Filtrar por año de nacimiento")
años_nacimiento = list(range(2025 - 75, 2025 - 14)) # Ajustado para el año actual
if filtrar_año_nacimiento:
    año_seleccionado = st.sidebar.selectbox("Seleccione el año de nacimiento", años_nacimiento)
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == año_seleccionado]

# 8. Filtro por acceso a internet
filtrar_internet = st.sidebar.checkbox("Filtrar por acceso a internet")
if filtrar_internet:
    acceso = st.sidebar.radio("Seleccione si tiene acceso a internet", ["Sí", "No"])
    if acceso == "Sí":
        df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == True]
    elif acceso == "No":
        df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == False]

# 9. Filtro por ingresos nulos
filtrar_ingresos_nulos = st.sidebar.checkbox("Filtrar por ingresos nulos")
if filtrar_ingresos_nulos:
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

# 10. Filtro por rango de fechas de nacimiento
filtrar_rango_fechas = st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento")
fecha_min = pd.to_datetime('2010-04-21') - pd.Timedelta(days=75*365) # Aproximación
fecha_max = pd.to_datetime('2010-04-21') - pd.Timedelta(days=15*365) # Aproximación
if filtrar_rango_fechas:
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", fecha_min)
    fecha_fin = st.sidebar.date_input("Fecha de fin", fecha_max)
    if fecha_inicio and fecha_fin:
        df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))]

# --- Mostrar el DataFrame filtrado ---
st.title("DataFrame con Filtros Dinámicos")
st.dataframe(df_filtrado)

st.write(f"Número de filas en el DataFrame filtrado: {df_filtrado.shape[0]}")

st.header("Solución")
code="""
# --- Generación del DataFrame ---
fake = Faker('es_CO')
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)
n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',  # Caribe
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',  # Andina
            'Cali', 'Quibdó', 'Buenaventura',           # Pacífica
            'Villavicencio', 'Yopal',                    # Orinoquía
            'Leticia', 'Puerto Inírida'                  # Amazonía
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)}
df_nuevo = pd.DataFrame(data)
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])

# --- Barra lateral para los filtros ---
st.sidebar.header("Filtros Dinámicos")
df_filtrado = df_nuevo.copy() # Inicializamos con el DataFrame original

# 1. Filtro por rango de edad
filtrar_edad = st.sidebar.checkbox("Filtrar por rango de edad")
if filtrar_edad:
    min_edad, max_edad = st.sidebar.slider("Seleccione el rango de edad", 15, 75, (15, 75))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

# 2. Filtro por municipios específicos
filtrar_municipio = st.sidebar.checkbox("Filtrar por municipios")
municipios_opciones = ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida']
if filtrar_municipio:
    municipios_seleccionados = st.sidebar.multiselect("Seleccione los municipios", municipios_opciones)
    if municipios_seleccionados:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(municipios_seleccionados)]

# 3. Filtro por ingreso mensual mínimo
filtrar_ingreso_minimo = st.sidebar.checkbox("Filtrar por ingreso mensual mínimo")
if filtrar_ingreso_minimo:
    ingreso_minimo = st.sidebar.slider("Ingrese el ingreso mensual mínimo", 800000, 12000000, 800000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_minimo]

# 4. Filtro por ocupación
filtrar_ocupacion = st.sidebar.checkbox("Filtrar por ocupación")
ocupaciones_opciones = ['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico', 'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero']
if filtrar_ocupacion:
    ocupaciones_seleccionadas = st.sidebar.multiselect("Seleccione las ocupaciones", ocupaciones_opciones)
    if ocupaciones_seleccionadas:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(ocupaciones_seleccionadas)]

# 5. Filtro por tipo de vivienda no propia
filtrar_no_propia = st.sidebar.checkbox("Filtrar personas sin vivienda propia")
if filtrar_no_propia:
    df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

# 6. Filtro por nombres que contienen una cadena
filtrar_nombre = st.sidebar.checkbox("Filtrar por nombre")
if filtrar_nombre:
    texto_nombre = st.sidebar.text_input("Ingrese texto a buscar en el nombre")
    if texto_nombre:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto_nombre, case=False, na=False)]

# 7. Filtro por año de nacimiento específico
filtrar_año_nacimiento = st.sidebar.checkbox("Filtrar por año de nacimiento")
años_nacimiento = list(range(2025 - 75, 2025 - 14)) # Ajustado para el año actual
if filtrar_año_nacimiento:
    año_seleccionado = st.sidebar.selectbox("Seleccione el año de nacimiento", años_nacimiento)
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == año_seleccionado]

# 8. Filtro por acceso a internet
filtrar_internet = st.sidebar.checkbox("Filtrar por acceso a internet")
if filtrar_internet:
    acceso = st.sidebar.radio("Seleccione si tiene acceso a internet", ["Sí", "No"])
    if acceso == "Sí":
        df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == True]
    elif acceso == "No":
        df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == False]

# 9. Filtro por ingresos nulos
filtrar_ingresos_nulos = st.sidebar.checkbox("Filtrar por ingresos nulos")
if filtrar_ingresos_nulos:
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

# 10. Filtro por rango de fechas de nacimiento
filtrar_rango_fechas = st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento")
fecha_min = pd.to_datetime('2010-04-21') - pd.Timedelta(days=75*365) # Aproximación
fecha_max = pd.to_datetime('2010-04-21') - pd.Timedelta(days=15*365) # Aproximación
if filtrar_rango_fechas:
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", fecha_min)
    fecha_fin = st.sidebar.date_input("Fecha de fin", fecha_max)
    if fecha_inicio and fecha_fin:
        df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))]

# --- Mostrar el DataFrame filtrado ---
st.title("DataFrame con Filtros Dinámicos")
st.dataframe(df_filtrado)

st.write(f"Número de filas en el DataFrame filtrado: {df_filtrado.shape[0]}")
 """
st.code(code, language='python')