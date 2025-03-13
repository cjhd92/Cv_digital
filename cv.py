import streamlit as st
import os
from PIL import Image

# Configurar la página con un diseño elegante
st.set_page_config(page_title="Mi CV Digital", page_icon="📄", layout="wide")

# Imagen de perfil y barra lateral
with st.sidebar:
    st.image("https://via.placeholder.com/150", width=150)
    st.title("César Javier Herrera Díaz")
    st.subheader("Ingeniero de Software | Data Engineer")
    
    # Información de contacto con iconos
    st.write("✉️ **Email:** cjhd92@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/cjhd92)")
    st.write("📍 Galicia, España")
    
    # Descargar CV en PDF si existe
    cv_path = "Cv.pdf"
    if os.path.exists(cv_path):
        with open(cv_path, "rb") as pdf:
            st.download_button("📥 Descargar CV en PDF", pdf, "Cv.pdf", "application/pdf")
    else:
        st.warning("⚠️ Archivo de CV no encontrado. Asegúrate de subirlo.")

# Sección de presentación con iconos y diseño profesional
st.header("Perfil Profesional")
st.write(
    "Ingeniero de software con experiencia en procesamiento de grandes volúmenes de datos, desarrollo de procesos ETL y gestión de bases de datos SQL. "
    "Especializado en el desarrollo de soluciones basadas en Python y en la aplicación de inteligencia artificial y modelos matemáticos para la clasificación y análisis de datos. "
    "Experiencia en visualización de datos mediante herramientas avanzadas, optimización de bases de datos y migración de sistemas.")



col1, col2 = st.columns([1, 4])

with col1:
    st.markdown("""
### Experiencia Laboral
<div style="width: 100%; border-bottom: 3px solid #007acc; margin-top: 0px;"></div>
""", unsafe_allow_html=True)

with col2:
    st.write("")  # Línea en blanco

st.write("")  # Línea en blanco
st.write("")  # Línea en blanco


st.subheader("📅 2022 - 2025     Proyecto de Movilidad Pública")

st.write("✔ Desarrollo de un sistema de estimación de matrices origen-destino para redes de transporte público complejas.")
st.write("✔ Desarrollo de un sistema de estimación de matrices origen-destino para redes de transporte público complejas.")
st.write("✔ Procesamiento y análisis de datos: Integración y transformación de múltiples formatos de datos, incluyendo GTFS.")
st.write("✔ Implementación de modelos predictivos para extrapolar patrones de movilidad.")
st.write("✔ Creación de una aplicación visual con gráficos dinámicos para la gestión del transporte público.")


st.subheader("📅 2019 - 2021     Proyecto de Tratamiento de Agua")

st.write("✔ Gestión y análisis de datos de sensores industriales (temperatura, presión, calidad del agua).")
st.write("✔ Desarrollo de sistemas de monitoreo en tiempo real, almacenamiento en SQL y procesamiento ETL.")
st.write("✔ Creación de dashboards e históricos para optimización del proceso y mejora de eficiencia operativa.")

st.write("")  # Línea en blanco
st.write("")  # Línea en blanco

col3, col4 = st.columns([1, 4])

with col3:
    st.markdown("""
###  Educación
<div style="width: 100%; border-bottom: 3px solid #007acc; margin-top: 0px;"></div>
""", unsafe_allow_html=True)

with col4:
    st.write("")  # Línea en blanco

st.write("")  # Línea en blanco
st.write("")  # Línea en blanco

st.write("📚 **Máster en Informática Industrial y Robótica** - Universidad de Coruña (2022 - 2023)")
st.write("📚 **Ingeniero Automático** - Universidad Tecnológica de la Habana, CUJAE (2012 - 2016)")

st.write("")  # Línea en blanco
st.write("")  # Línea en blanco


st.subheader(" Habilidades Técnicas")
st.markdown("<div style='border-bottom: 3px solid #007acc; width: 20%; margin-bottom: 15px;'></div>", unsafe_allow_html=True)

# Habilidades con información adicional
skills = {
    "Python": "Librerías: Pandas, NumPy, Scikit-learn, Matplotlib,Openpyxl",
    "SQL": "Bases de datos: MySQL, SQLite",
    "Machine Learning": "Herramientas: TensorFlow, Scikit-learn",
    "ETL": "Procesos:  Pandas",
    "Power BI": "Dashboards, Reportes dinámicos",
    "Data Visualization": "Herramientas: Matplotlib, Seaborn, Plotly",
    "Streamlit": "Framework para dashboards interactivos",
    "JavaScript": "Frameworks: React",
    "TypeScript": "Extensión tipada de JavaScript",
    "Angular": "Framework para desarrollo web",
    "React": "Framework de UI basado en componentes",
    "NestJS": "Framework para APIs en Node.js"
}

# Aplicar estilos de botón con tooltips
st.markdown("<style>.skill-badge { display: inline-block; background-color: #007acc; color: white; padding: 8px 15px; margin: 5px; border-radius: 10px; font-size: 16px; cursor: pointer; }</style>", unsafe_allow_html=True)

skills_html = " ".join([f"<span class='skill-badge' title='{info}'>{skill}</span>" for skill, info in skills.items()])
st.markdown(skills_html, unsafe_allow_html=True)





st.subheader("📌 Proyectos en GitHub")

proyectos = [
    {"nombre": "📊 Análisis de Datos con Pandas", "url": "https://github.com/tu_usuario/proyecto1"},
    {"nombre": "🤖 Modelo de Machine Learning", "url": "https://github.com/tu_usuario/proyecto2"},
    {"nombre": "📈 Dashboard en Streamlit", "url": "https://github.com/cjhd92/Dashboard-Ventas-Tienda-Tech.git"},
    {"nombre": "🌐 API con FastAPI y PostgreSQL", "url": "https://github.com/tu_usuario/proyecto4"}
]

cols = st.columns(2)  # Divide en dos columnas

for i, proyecto in enumerate(proyectos):
    with cols[i % 2]:  # Alterna columnas
        st.markdown(f"""
        <div style="border: 1px solid #007acc; padding: 10px; border-radius: 10px; margin-bottom: 10px;">
            <h4 style="margin:0;">{proyecto['nombre']}</h4>
            <a href="{proyecto['url']}" target="_blank">🔗 Ver en GitHub</a>
        </div>
        """, unsafe_allow_html=True)


# Footer con diseño profesional
st.write("---")
st.write("💻 Desarrollado con ❤️ usando **Streamlit**")


