# Documentación de Notebooks

Este repositorio contiene varios cuadernos de Jupyter que se utilizan para diferentes propósitos.

## Notebooks

###  Web scraping `/scraping`

| Nombre del Cuaderno | Descripción |
|---------------------|-------------|
| `scraping_pccomponentes.ipynb` | Este cuaderno se utiliza para realizar scraping de datos de componentes de PC. |
| `scraping_processors.ipynb` | Este cuaderno se utiliza para realizar scraping de datos de procesadores. |
| `scraping_pcpartpicker.ipynb` | Este cuaderno se utiliza para realizar scraping de datos de PCPartPicker. |


### Datasets

| Nombre del Cuaderno | Descripción |
|---------------------|-------------|
| `dataset_01.ipynb` | Este cuaderno se utiliza para crear el conjunto de datos que se empleará para entrenar nuestro modelo. |
| `dataset_02.ipynb` | Este cuaderno se utiliza para descargar las imágenes y crear el conjunto de datos. |
| `dataset_03.ipynb` | Este cuaderno se utiliza para crear el dataset definitivo. |

## 🐳 Ejecutar con Docker

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