![logo](/img/HardVisionAI.png)
# 🖥️ HardVisionAI

**HardVisionAI** es un modelo de visión artificial diseñado para identificar componentes de PC a partir de imágenes y extraer automáticamente información técnica relevante, como marca, modelo y especificaciones.

Este modelo forma parte de nuestro **Trabajo Fin de Máster (TFM)** del Máster de FP en Inteligencia Artificial y Big Data, contribuyendo al desarrollo de herramientas avanzadas de análisis y procesamiento de información.

En este proyecto estará disponible una demo del modelo en la plataforma Streamlit, permitiendo realizar pruebas interactivas y explorar su funcionamiento.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hardvisionai.streamlit.app/)

## 🗃️ Obtención de datos

Los datos utilizados para entrenar los modelos se obtuvieron mediante técnicas de **web scraping** y fueron posteriormente recopilados y procesados para su análisis y preparación en este proyecto.

Las fuentes de información incluyeron sitios web especializados en componentes de PC:  

- [PCComponentes](https://www.pccomponentes.com)  
- [TechPowerUp](https://www.techpowerup.com)  
- [PCPartPicker](https://pcpartpicker.com)

Estos portales proporcionan información detallada sobre marcas, modelos y especificaciones técnicas, lo que permitió construir un dataset representativo y de calidad para el entrenamiento del modelo.

## 🐍 Stack Tecnológico

![Python Version](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)

El proyecto HardVisionAI utiliza **Python 3.12** para todo el código:

- Web scraping
- Procesamiento de datasets
- Modelos OCR
- Entrenamiento de redes neuronales
- Streamlit

## 🐳 Ejecutar Streamlit con Docker

### 1. Construir y levantar el contenedor

```bash
docker-compose up --build
```

### 2. Abrir en el navegador

```
http://localhost:8501
```

## 📂 Estructura del proyecto

```text
HardVisionAI/
│
├── data/               # CSV, JSON e imágenes
├── img/                # Logos y capturas
├── models/             # Modelo entrenado
├── notebooks/          # Cuadernos Jupyter
├── requirements.txt    # Dependencias Python 3.12
├── app.py              # Integración del modelo
├── streamlit_app.py    # Demo Streamlit
├── Dockerfile          # Contenedor Streamlit
├── docker-compose.yml  # Levantar demo con Docker
├── .gitignore          # Archivos ignorados por Git
├── LICENSE             # Licencia personalizada
└── README.md           # Este archivo
```

## 👤 Créditos

### 👨‍💻 Autores del proyecto

* [Alejandro Barrionuevo Rosado](https://github.com/Alejandro-BR)
* [Alvaro López Guerrero](https://github.com/Alvalogue72)
* [Andrei Munteanu Popa](https://github.com/andu8705)

Máster de FP en Inteligencia Artifical y Big Data - CPIFP Alan Turing - `Curso 2025/2026`

<img src="./img/alan_turing.png" width="150"/>

### 📄 Licencia

![License](https://img.shields.io/badge/license-HardVisionAI%20Custom-blue)

Este proyecto está protegido por derechos de autor. No se permite su uso, copia, modificación, distribución ni creación de obras derivadas sin autorización expresa de los autores.

© 2026 Alejandro-BR, Alvalogue72, andu8705. Todos los derechos reservados.  
Para consultas o permisos especiales, contactar a: [latencyzero.tfm@gmail.com](mailto:latencyzero.tfm@gmail.com)

---

⭐ Si te ha gustado este repo, dale una estrellita 😉

![GitHub Repo Stars](https://img.shields.io/github/stars/Latency-Zero-tfm/HardVisionAI?style=social)
![Last Commit](https://img.shields.io/github/last-commit/Latency-Zero-tfm/HardVisionAI)
![GitHub Issues](https://img.shields.io/github/issues/Latency-Zero-tfm/HardVisionAI)
