# Agente Inteligente para Responder Preguntas de un Documento

Este proyecto implementa un sistema basado en Retrieval Augmented Generation (RAG) para responder preguntas basadas en un documento específico. Utiliza el modelo de lenguaje Ollama para la generación y recuperación de información. El sistema está expuesto como una API RESTful utilizando Flask.

## Características

- **Recuperación y Generación**: Utiliza el enfoque RAG para buscar y generar respuestas a preguntas basadas en un documento.
- **API RESTful**: Exposición del modelo RAG como un servicio web mediante una API RESTful.
- **Soporte para PDF**: Capacidad para procesar documentos en formato PDF.

## Requisitos

- Python 3.6+
- Flask
- Dependencias del proyecto (`rag_model`, `langchain_community`, `ollama`)

## Instalación

1. Clonar el repositorio:

git clone https://github.com/EnzoSz/prueba-tecnica-musa.git

2. Crear un entorno virtual (recomendado):

python -m virtualenv  venv

activar el entorno:
en bash:
source venv/Scripts/activate

3. Instalar las dependencias:

pip install -r requirements.txt

## Uso

Para iniciar la aplicación:

python app.py

La API estará disponible en `http://localhost:5000/response`. Para enviar una pregunta, realiza una solicitud POST con el cuerpo JSON `{ "question": "tu_pregunta_aqui" }`.

## Pruebas

Se incluyen pruebas unitarias para el modelo RAG y la API. Ejecutarlas con:

python -m unittest discover

## Contribución

Contribuciones son bienvenidas. Por favor, abre un issue o haz un pull request.
