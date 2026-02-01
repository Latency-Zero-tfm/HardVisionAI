import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
import easyocr
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image

# Configuracion
st.set_page_config(page_title="HardVision AI", page_icon="🖥️", layout="centered")

label_map = {
    0: 'motherboard',
    1: 'gpu',
    2: 'cpu',
    3: 'hard_drive',
    4: 'ram',
    5: 'pc_case',
    6: 'power_supply',
    7: 'liquid_cooling', 
    8: 'case_fan',
    9: 'cpu_fan', 
    10: 'sound_card'
}

translation_map = {
    'motherboard': 'Placa Base',
    'gpu': 'Tarjeta Gráfica (GPU)',
    'cpu': 'Procesador (CPU)',
    'hard_drive': 'Disco Duro / SSD',
    'ram': 'Memoria RAM',
    'pc_case': 'Torre / Caja PC',
    'power_supply': 'Fuente de Alimentación',
    'liquid_cooling': 'Refrigeración Líquida',
    'case_fan': 'Ventilador de Caja',
    'cpu_fan': 'Disipador / Ventilador CPU',
    'sound_card': 'Tarjeta de Sonido'
}

modelo_ruta = 'models/components_pc_model.keras'

# Carga de recursos (cache)
@st.cache_resource
def load_resources():
    try:
        model = load_model(modelo_ruta)
        reader = easyocr.Reader(['en'], gpu=True) 
        return model, reader
    
    except:
        st.error(f"Error cargando recursos.")
        return None, None

model, reader = load_resources()

# Funciones de procesamiento
def process_images(img_array):
    try:
        # Resize
        img_resized = cv2.resize(img_array, (230, 230))
        
        # Convertir a escala de grises (Si la imagen viene de PIL/Streamlit es RGB)
        if len(img_resized.shape) == 3:
            img_gray = cv2.cvtColor(img_resized, cv2.COLOR_RGB2GRAY)
        else:
            img_gray = img_resized

        # Normalización y vectorización
        img_norm = img_gray.astype('float32') / 255.0
        
        # Expandir dimensiones (1, 230, 230, 1)
        img_processed = np.expand_dims(img_norm, axis=0)
        img_processed = np.expand_dims(img_processed, axis=-1)
        
        return img_processed, img_gray
    
    except:
        st.error(f"Error procesando la imagen.")
        return None, None

# Interfaz de usuario
st.title("HardVision AI")
st.markdown("Sube una imagen de un componente de PC para identificarlo y extraer sus especificaciones.")

uploaded_file = st.file_uploader("Sube tu imagen", type=["png", "jpg", "jpeg", "webp"])

if uploaded_file is not None and model is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_container_width=True)
    
    img_array = np.array(image)
    
    with st.spinner('Analizando componente y extrayendo texto...'):
        
        # Procesamiento
        processed_input, img_gray_display = process_images(img_array)
        
        # B. Prediccion
        predictions = model.predict(processed_input)
        predicted_index = np.argmax(predictions)
        confidence_scores = predictions[0]
        
        ingles_label = label_map[predicted_index]
        label_espanol = translation_map[ingles_label]
        
        # OCR
        ocr_results = reader.readtext(img_array, detail=0)
        ocr_results_upper = [text.upper() for text in ocr_results]
        
        # Intel/AMD
        is_processor = ingles_label == 'cpu'
        found_brand = None
        if is_processor:
            if "INTEL" in ocr_results_upper: found_brand = "INTEL"
            elif "AMD" in ocr_results_upper: found_brand = "AMD"

    # Resultados
    st.divider()
    
    # Cuadrado verde con el resultado
    st.success(f"**Componente detectado:** {label_espanol.upper()}")
    
    # Expandir
    with st.expander("Ver detalles técnicos y analisis gráfico"):
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Informacion extraida")
            if not ocr_results:
                st.info("No se ha detectado ningun dato en la imagen.")
            else:
                data_to_list = ocr_results
                if is_processor and found_brand:
                    st.markdown(f"**Procesador: {found_brand}**")
                    data_to_list = [x for x in ocr_results if x.upper() != found_brand]
                
                if not data_to_list:
                    st.caption("(No hay más datos adicionales)")
                else:
                    for i, data in enumerate(data_to_list, 1):
                        st.write(f"**{i}.** {data}")

        with col2:
            st.subheader("Vision de la IA")
            st.image(img_gray_display, caption="Input del modelo", clamp=True, channels='GRAY')

        # Grafica
        st.divider()
        st.subheader("Confianza del modelo")
        
        label_espanols_list = [translation_map[label_map[i]] for i in range(len(label_map))]
        explode = [0.1 if i == predicted_index else 0 for i in range(len(confidence_scores))]
        colors = plt.cm.Pastel1(np.linspace(0, 1, len(label_espanols_list)))

        fig, ax = plt.subplots(figsize=(10, 5))
        wedges, texts, autotexts = ax.pie(
            confidence_scores, 
            autopct=lambda p: f'{p:.1f}%' if p > 5 else '',
            startangle=140,
            explode=explode,
            colors=colors,
            pctdistance=0.85,
            shadow=True,
            wedgeprops=dict(width=0.5, edgecolor='w')
        )
        
        plt.setp(autotexts, size=9, weight="bold", color="black")
        ax.set_title(f"Prediccion: {label_espanol}", fontsize=14, fontweight='bold')
        ax.legend(wedges, label_espanols_list, title="Categorias", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        
        st.pyplot(fig)

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