# Documentación de Notebooks

Este repositorio contiene todos los cuadernos de Jupyter utilizados a lo largo del proyecto **HardVisionAI**, desde la obtención de datos hasta el procesamiento OCR y entrenamiento de modelos de visión artificial.



## 📒 Notebooks principales

Estos notebooks contienen todos los pasos del proyecto, desde la recopilación y limpieza de datos hasta el entrenamiento de modelos y extracción de información mediante OCR.

| Nombre del Cuaderno | Descripción |
|---------------------|-------------|
| `create_and_clean_dataset.ipynb` | Crea el dataset original con las URLs de las imágenes y sus etiquetas (labels). |
| `dataset_processing.ipynb` | Transforma el dataset guardando imágenes localmente y convirtiendo etiquetas a valores numéricos. |
| `model_training.ipynb` | Entrenamiento de la red neuronal para la clasificación de componentes de PC. |
| `model_ocr.ipynb` | Aplica OCR a las imágenes del dataset para extraer texto, marcas, modelos y especificaciones.|
| `app.ipynb` | Integra `model_ocr.ipynb` y `model_training`, usando el código para la interfaz de Streamlit. |

## 🌐 Web scraping `/scraping`

Estos notebooks realizan la extracción de datos desde distintas fuentes web de componentes de PC.

| Nombre del Cuaderno | Descripción |
|---------------------|-------------|
| `scraping_pccomponentes.ipynb` | Realiza scraping de datos de componentes de PC desde PCComponentes. |
| `scraping_processors.ipynb` | Realiza scraping de datos específicos de procesadores. |
| `scraping_pcpartpicker.ipynb`| Realiza scraping de datos de componentes desde PCPartPicker. |

## 🐳 Ejecutar con Docker

Utiliza el entorno proporcionado por la imagen `Dockerfile.jupyter`.


### 1. Construir y levantar el contenedor

> [!IMPORTANT]  
> Ejecutar desde la raíz del proyecto.
>

```bash
docker build -f notebooks/Dockerfile.jupyter -t jupyter-python notebooks
```

```bash
docker run -p 8888:8888 -v ${PWD}:/app jupyter-python
```

### 2. Abrir en el navegador

```
http://localhost:8888/tree
```
