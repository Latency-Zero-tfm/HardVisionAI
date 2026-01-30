# Documentación de Notebooks

Este repositorio contiene varios cuadernos de Jupyter que se utilizan para diferentes propósitos.

## Notebooks

| Nombre del Cuaderno | Descripción |
|---------------------|-------------|
| `create_and_clean_dataset.ipynb` | ... |
| `dataset_processing.ipynb` | ... |
| `model_training.ipynb` | ... |

###  Web scraping `/scraping`

| Nombre del Cuaderno | Descripción |
|---------------------|-------------|
| `scraping_pccomponentes.ipynb` | Este cuaderno se utiliza para realizar scraping de datos de componentes de PC. |
| `scraping_processors.ipynb` | Este cuaderno se utiliza para realizar scraping de datos de procesadores. |
| `scraping_pcpartpicker.ipynb` | Este cuaderno se utiliza para realizar scraping de datos de PCPartPicker. |

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