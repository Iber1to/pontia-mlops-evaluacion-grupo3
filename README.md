# Simple ML Training Project
This project trains a RandomForest model on tabular data.
test
test - 2

# Título del proyecto

Descripción breve del proyecto.

## Tabla de contenidoes

- [Flujo de Trabajo (CI/CD)](#flujo-de-trabajo-cicd)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplos](#ejemplos)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Contacto](#contacto)
- [Referencias](#referencias)

## Estructura del Proyecto
El código sigue una arquitectura modular, separando la lógica de entrenamiento, la infraestructura de despliegue y la validación de calidad en capas independientes:

* **`src/`**: Núcleo del proyecto que contiene la lógica de ciencia de datos.
    * **`data_loader.py`**: Funciones para la ingesta y preprocesamiento de los datos.
    * **`model.py`**: Definición, configuración e instanciación del modelo.
    * **`evaluate.py`**: Módulo de evaluación, muestra precision y clasificación.
    * **`main.py`**: Orquestador del pipeline; ejecuta el flujo completo desde la carga hasta el entrenamiento.
* **`deployment/`**: Infraestructura necesaria para servir el modelo en producción.
    * **`app/main.py`**: Punto de entrada de la **API**. Gestiona las peticiones y devuelve predicciones y metricas.
    * **`requirements.txt`**: Dependencias para el entorno de ejecución. Modelo ya entrenado asi que deben ser lo mas ligeras posibles.
* **`unit_tests/`**: Pruebas unitarias aisladas para garantizar que cada componentem funciona correctamente.
* **`model_tests/`**: Pruebas de validación del modelo entrenado, asegurando que el artefacto final cumple con los umbrales de calidad requeridos.
* **`pytest.ini`**: Archivo de configuración para la automatización de la suite de pruebas con Pytest.
* **`requirements.txt`**: Listado completo de dependencias, necesarias tanto para desarrollo, entrenamiento y produccion.
* **`.gitignore`**: Especificación de archivos excluidos del repositorio.


## Ciclo de Vida (CI/CD)

El proyecto asegura la integridad del modelo mediante el siguiente flujo:

1. **Validación de Código:** Ejecución de `unit_tests` para verificar la lógica de `src/`.
2. **Entrenamiento:** Generación del modelo mediante el pipeline principal.
3. **Validación de Modelo:** Los `model_tests` certifican la precisión del RandomForest antes de su liberación.
4. **Despliegue:** La carpeta `deployment/` toma el modelo validado para servirlo mediante una API.

## Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone git@github.com:Iber1to/pontia-mlops-evaluacion-grupo3.git
   ```
2. **Configurar el entorno virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Ejecución y Despliegue

### Despliegue Local
Para probar el pipeline o la API en tu máquina local:

1. **Instalar dependencias:** `pip install -r requirements.txt`
2. **Entrenar y probar:** `python src/main.py && pytest`
3. **Levantar API:** `uvicorn deployment.app.main:app --reload`


### Despliegue en Render
Este proyecto utiliza **Infrastructure as Code (IaC)** mediante un archivo `render.yaml`. Esto permite un despliegue facil con toda la configuración predefinida.


## Documentación de la API

La API gestiona automáticamente el ciclo de vida de los artefactos. Al iniciar, descarga la versión más reciente del modelo (`model.pkl`), el escalador (`scaler.pkl`) y los encoders (`encoders.pkl`) directamente desde los **Releases de GitHub**.

### Endpoints Principales

| Endpoint | Método | Descripción |
| --- | --- | --- |
| /health | GET | Verifica que el servicio esté activo y listo. |
| /predict | POST | Procesa datos y devuelve la predicción del modelo. |
| /metrics | GET | Expone el conteo total de predicciones (PlainText). |
| /docs | GET | Documentación interactiva y pruebas en vivo (Swagger). |
> **Interactividad:** Puedes probar la API en vivo accediendo a `/docs` (Swagger UI) una vez desplegada.

## Ejemplos




## Licencia



## Contacto



## Referencias

