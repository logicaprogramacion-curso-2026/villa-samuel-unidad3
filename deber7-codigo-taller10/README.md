# Sistema de Evaluación Docente con IA

## Descripción

Sistema desarrollado en Python que permite analizar actividades
realizadas por docentes mediante inteligencia artificial utilizando
Ollama.

El sistema recibe el nombre del docente, la materia y una cantidad
variable de actividades realizadas.

Posteriormente, las actividades son analizadas por un modelo de
inteligencia artificial.

## Criterios de evaluación

El sistema analiza tres criterios:

### 1. Recursos digitales

Analiza el uso, frecuencia, variedad y finalidad pedagógica de
los recursos digitales utilizados.

### 2. Evaluación

Analiza los métodos e instrumentos utilizados para evaluar el
aprendizaje, incluyendo rúbricas, retroalimentación,
autoevaluación y coevaluación.

### 3. Empoderamiento del estudiante

Analiza la participación, autonomía, investigación,
colaboración, creatividad, pensamiento crítico y toma
de decisiones.

## Niveles

Cada criterio recibe un nivel:

- Nivel 1: Bajo / Necesita mejorar
- Nivel 2: Medio / Aceptable
- Nivel 3: Alto / Excelente

La cantidad de actividades no determina por sí sola el nivel.

El sistema considera principalmente la calidad, evidencia,
consistencia y propósito pedagógico.

## Inteligencia artificial

El sistema utiliza Ollama como servidor local de inteligencia
artificial.

Modelo utilizado:

`llama3.2`

## Requisitos

- Python 3.11 o superior
- Ollama
- Modelo llama3.2

## Instalación

Verificar Python:

```bash
python --version