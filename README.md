# PLN_Proyecto Gerardo Diaz

# 🧠 Auto-Glossary Builder & Q-A Assistant

Este proyecto implementa una herramienta automática para construir un glosario técnico interactivo a partir de un conjunto de documentos en texto plano. Fue desarrollado como parte del curso **Procesamiento de Lenguaje Natural (Q2-2025)** en la **Universidad Tecnológica Centroamericana (UNITEC)**.

---

## 🎯 Objetivo General

- Aplicar técnicas de PLN como extracción de términos, agrupación por similitud, análisis de subpalabras y generación automática de definiciones para construir un glosario interactivo.
- Integrar una **interfaz de línea de comandos (CLI)** para consultar los términos de forma amigable.
- Utilizar un **modelo LLM local con Ollama** para completar definiciones y ejemplos.

---

## 🧱 Estructura del Proyecto

project-root/
├── corpus/ # Archivos de texto fuente (2–5 archivos .txt)
│ ├── 001.txt
│ ├── 002.txt
├── extract_terms.py # Paso 2: Regex para extraer términos
├── build_glossary.py # Paso 3-4: Agrupar variantes y aplicar BPE
├── define_terms.py # Paso 5: Consultar LLM y completar el glosario
├── cli.py # Paso 6: Interfaz de línea de comandos
├── glossary.json # Glosario generado en formato estructurado
└── README.md # Este archivo



---

## 🛠️ Pasos Realizados

### 1. 📁 Corpus Collection
Se creó una carpeta `corpus/` con documentos relacionados a deportes, con un total de 500–1000 palabras.

### 2. 🔍 Term Extraction (Regex Mining)
Usamos expresiones regulares para extraer:
- Palabras técnicas (`tokenization`)
- Formatos `CamelCase`, `snake_case`
- Siglas (`NLP`, `AI`)
- Palabras de 4+ letras

Se generó el archivo `terms.txt` con los términos y sus frecuencias.

### 3. 🧠 Variant Consolidation (Levenshtein Distance)
Agrupamos términos similares con una distancia de Levenshtein ≤ 3.

### 4. 🧩 Subword Analysis (Tiny BPE)
Dividimos los términos canónicos en subpalabras frecuentes usando un BPE simplificado.


### 5. 🤖 LLM Integration with Ollama
Usamos `mistral` con Ollama para generar definiciones y ejemplos en español, enfocados en el contexto deportivo. Se integró una petición a la API con un prompt estructurado que devuelve JSON.


### 6. 🖥️ Interfaz CLI
Creamos cli.py, una interfaz interactiva donde el usuario puede:

1: Listar términos

2: Definir un término

3: Buscar por texto con coincidencia aproximada

4: Salir del sistema


###  ⚙️ Requisitos del Proyecto
Python 3.10+

Librerías:

requests

python-Levenshtein

Ollama instalado y corriendo el modelo mistral o orca-mini (si tu PC tiene poca RAM)


### 📦 Archivos generados
terms.txt: lista de términos extraídos y frecuencia

glossary.json: contiene todos los términos procesados con variantes, tokens, definición y ejemplo

### ✍️ Autor
Estudiante: Gerardo Andre Diaz Urraco

Curso: Procesamiento de Lenguaje Natural (Q2-2025)

Docente: Ing. Iván de Jesús Deras Tábora

Universidad: Universidad Tecnológica Centroamericana (UNITEC)
