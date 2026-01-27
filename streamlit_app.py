import streamlit as st
import pandas as pd

# TODO: Cambiar datos simulados por predicciones reales del modelo entrenado
componente = {
    "Tipo": "Procesador",
    "Marca": "Intel",
    "Modelo": "Core i7-12700K",
    "Precio": "349.99 €",
}

st.set_page_config(page_title="HardVision AI", page_icon="🖥️", layout="centered")

st.title("HardVision AI")
uploaded_file = st.file_uploader("Sube tu imagen", type=["png", "jpg", "jpeg", "webp"])
    
if uploaded_file:
    st.image(uploaded_file, caption=f"{componente['Tipo']} {componente['Marca']} {componente['Modelo']}")
    st.divider() 
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Componente detectado")
        st.success(f"**Tipo de componente:** {componente['Tipo']}")
        st.write(f"**Marca:** {componente['Marca']}")
        st.write(f"**Modelo:** {componente['Modelo']}")
        st.write(f"**Precio estimado:** {componente['Precio']}")
    with col2:
        st.subheader("Datos en formato JSON")
        componente_json = pd.Series(componente).to_json(indent=4)
        st.code(componente_json, language='json')
        st.download_button(
            label="Descargar JSON",
            data=componente_json,
            file_name='componente.json',
            mime='application/json'
        )
else:
    
    st.subheader("¿Cómo empezar?")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.markdown("### 1. Sube")
        st.write("Carga una foto clara de tu componente o hardware. Cuanta más luz y centrado esté la foto, mejor precisión.")
        
    with col_b:
        st.markdown("### 2. Analiza")
        st.write("Nuestra IA extrae patrones visuales, logotipos y números de serie de la imagen del componente.")
        
    with col_c:
        st.markdown("### 3. Obtén")
        st.write("Recibe la información del tipo, modelo, precio de mercado y ficha técnica del componente en segundos.")
        
    with st.expander("🔍 Ver detalles de la tecnología"):
        st.write(" Esta herramienta ha sido entrenada con un dataset de más de 10,000 imágenes de componentes. Utilizamos un modelo de **Machine Learning** optimizado para detectar hardware, capaz de diferenciar componentes de distintos tipos.")
        st.info("💡 **Consejo:** Intenta que el componente ocupe al menos el 60% del encuadre para mejores resultados.")   

# Footer
st.divider()
_, col_center, _ = st.columns([1, 4, 1])

with col_center:
    st.caption("#### HardVision AI © 2026", text_alignment="center")
    st.caption("Desarrollado por estudiantes de Alan Turing", text_alignment="center")
    st.caption("*Andrei Munteanu Popa • Alejandro Barrionuevo Rosado • Álvaro López Guerrero*", text_alignment="center")