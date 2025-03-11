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
st.header("💡 Sobre mí")
st.write(
    "Ingeniero de software con experiencia en procesamiento de grandes volúmenes de datos, desarrollo de procesos ETL y gestión de bases de datos SQL. "
    "Especializado en el desarrollo de soluciones basadas en Python y en la aplicación de inteligencia artificial y modelos matemáticos para la clasificación y análisis de datos. "
    "Experiencia en visualización de datos mediante herramientas avanzadas, optimización de bases de datos y migración de sistemas.")

# Sección de habilidades con diseño mejorado
st.header("🛠️ Habilidades Técnicas")
skills = ["Python", "SQL", "Machine Learning", "ETL", "Power BI", "Data Visualization", "Streamlit", "JavaScript", "TypeScript", "Angular", "React", "NestJS"]
st.write("✅ " + " | ✅ ".join(skills))

# Experiencia laboral con diseño estructurado
st.header("💼 Experiencia")

st.subheader("🔹 Proyecto de Movilidad Pública")
st.write("📅 2022 - 2023")
st.write("✔ Desarrollo de un sistema de estimación de matrices origen-destino para redes de transporte público complejas.")
st.write("✔ Procesamiento y análisis de datos: Integración y transformación de múltiples formatos de datos, incluyendo GTFS.")
st.write("✔ Implementación de modelos predictivos para extrapolar patrones de movilidad.")
st.write("✔ Creación de una aplicación visual con gráficos dinámicos para la gestión del transporte público.")

st.subheader("🔹 Proyecto de Tratamiento de Agua")
st.write("📅 2019 - 2021")
st.write("✔ Gestión y análisis de datos de sensores industriales (temperatura, presión, calidad del agua).")
st.write("✔ Desarrollo de sistemas de monitoreo en tiempo real, almacenamiento en SQL y procesamiento ETL.")
st.write("✔ Creación de dashboards e históricos para optimización del proceso y mejora de eficiencia operativa.")

# Educación
st.header("🎓 Educación")
st.write("📚 **Máster en Informática Industrial y Robótica** - Universidad de Coruña (2022 - 2023)")
st.write("📚 **Ingeniero Automático** - Universidad Tecnológica de la Habana, CUJAE (2012 - 2016)")

# Footer con diseño profesional
st.write("---")
st.write("💻 Desarrollado con ❤️ usando **Streamlit**")
