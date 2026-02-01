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

## 🐍 Versiones de Python

El proyecto **HardVisionAI** utiliza **dos versiones de Python**, cada una para diferentes módulos:

* **Python 3.14.0**
  Utilizado para la mayor parte del proyecto, incluyendo:

  * Web scraping
  * Procesamiento de datasets
  * Modelos OCR

* **Python 3.12.0**
  Utilizado únicamente para el **entrenamiento de la red neuronal**, debido a compatibilidades con algunas librerías específicas.


## ⚡ Ejecutar notebooks en entorno local

1. **Crear el entorno virtual**

   ```bash
   python -m venv venv
   ```

2. **Activar el entorno**

   * En **Linux / macOS**:

     ```bash
     source venv/bin/activate
     ```
   * En **Windows**:

     ```cmd
     venv\Scripts\activate
     ```

3. **Instalar dependencias**

   * **Para la mayoría de los notebooks** (Python 3.14 o entorno principal):

     ```bash
     pip install -r requirements.txt
     ```

   * **Para el notebooks de entrenamiento de modelos** (requieren Python 3.12):

     ```bash
     pip install -r requirements-py12.txt
     ```

4. **Ejecutar Jupyter Notebook**

   ```bash
   pip install notebook
   jupyter notebook
   ```
