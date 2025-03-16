import streamlit as st
import os
from PIL import Image, ImageDraw


# Configurar la página con un diseño elegante
st.set_page_config(page_title="Mi CV Digital", page_icon="📄", layout="wide")



 
def redondear_esquinas(imagen_path, size=(220, 255), radio=10):
    img = Image.open(imagen_path).convert("RGBA").resize(size)

    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    
    draw.rounded_rectangle([0, 0, size[0], size[1]], radius=radio, fill=255)

    img_redondeada = Image.new("RGBA", size, (0, 0, 0, 0))
    img_redondeada.paste(img, (0, 0), mask)

    return img_redondeada
 



# Imagen de perfil y barra lateral
with st.sidebar:
    #st.image("foto.jpg", width=150)
    try:
        
        colf1, colf2,colf3 = st.columns([1, 2,1])

        with colf1:
            pass
        with colf2:
            #img_redonda = redondear_imagen("foto2.jpg")
            #st.image(img_redonda, width=150)

            img_redonda = redondear_esquinas("foto.jpg", size=(250, 300), radio=100)
            st.image(img_redonda, width=220)

        with colf3:
            pass
            

       
     

        # Mostrar imagen centrada
        
    except Exception as e:
        st.error(f"Error al procesar la imagen: {e}")
    
    st.title("César Javier Herrera Díaz")
    st.subheader("Ingeniero de Software | Data Engineer")
    
    # Información de contacto con iconos
    st.write("✉️ **Email:** cjhd92@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/cjhd92)")
    st.write("📍 Coruña, _España_")
    st.write("🪪 Permiso de conducción (_B_)")
    
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


colp1,colp2 = st.columns([90, 10])
with colp1:
    st.subheader("Sistema de estimación de matrices origen-destino en transporte público")
with colp2:
    st.write("2022 - Actualidad")

#st.subheader("📅 2022 - Actualidad:      Universidad de la Coruña")
st.markdown(
    "<p style='font-size:18px; font-weight: normal; color: #7F8C8D;'>Universidad de la Coruña - Presencial</p>",
    unsafe_allow_html=True
)



st.write("✔ Desarrollo de un sistema de estimación de matrices origen-destino para redes de transporte público complejas.")
st.write("✔ Procesamiento y análisis de datos: Integración y transformación de múltiples formatos de datos, incluyendo GTFS.")
st.write("✔ Implementación de modelos predictivos para extrapolar patrones de movilidad.")
st.write("✔ Creación de una aplicación visual con gráficos dinámicos para la gestión del transporte público.")

colp3,colp4 = st.columns([90, 10])
with colp3:
    st.subheader("Procesamiento de Datos Industriales para la Eficiencia en Tratamiento de Agua")
with colp4:
    st.write("2019 - 2021")

#st.subheader("📅 2022 - Actualidad:      Universidad de la Coruña")
st.markdown(
    "<p style='font-size:18px; font-weight: normal; color: #7F8C8D;'>ESINES (Empresa de Servicios Ingenieros Especializados) - Presencial</p>",
    unsafe_allow_html=True
)

#st.subheader("📅 2019 - 2021     Proyecto de Tratamiento de Agua")

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
    {"nombre": "🤖 Estimación de Generación Eléctrica en Minieólica con IA", "url": "https://github.com/cjhd92/TMF.git"},
    {"nombre": "📈 Dashboard en Streamlit Tienda tecnológica", "url": "https://github.com/cjhd92/Dashboard-Ventas-Tienda-Tech.git"},
    {"nombre": "🌐 API Análisis del Clima", "url": "https://github.com/cjhd92/analisis-del-clima-con-api.git"}
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


