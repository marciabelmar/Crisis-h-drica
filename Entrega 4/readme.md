# Visualización de Datos de Calidad del Agua en Chile

Este repositorio contiene un script de Python para visualizar la tendencia de los niveles de bacteriología y turbiedad en el agua de Chile entre 2019 y 2023.

[Ver presentación en Youtube](https://youtu.be/l95x21-ekfQ)

## Descripción

La calidad del agua es un tema crucial en Chile, especialmente debido a la sequía y la industrialización, y central en mi investigación sobre la crisis hídrica en Ñuble. Este análisis utiliza datos sobre bacteriología y turbiedad para evaluar la calidad del agua a lo largo de varios años.

## Proceso de Selección de Datos y Visualización

### Paso 1: Selección de Datos

Para esta visualización, seleccionamos datos que reflejan la calidad del agua en Chile, específicamente los niveles de bacteriología y turbiedad. Estos indicadores son cruciales para entender la presencia de microorganismos y la claridad del agua, respectivamente.

#### Base de Datos Utilizada

- **Nombre**: Base de datos combinada
- **Formato**: CSV
- **Contenido**: Datos anuales sobre varios parámetros de calidad del agua en Chile desde 2019 hasta 2023.

### Paso 2: Procesamiento de Datos

1. **Carga de Datos**: Se utilizó la biblioteca `pandas` para cargar el archivo CSV en un DataFrame de Python.
2. **Extracción de Años**: Los datos contenían una columna con el formato "ResultadoAño", de la cual se extrajeron los años como enteros para facilitar el análisis temporal.
3. **Selección de Indicadores**: Se seleccionaron las columnas correspondientes a los niveles de bacteriología y turbiedad.

### Paso 3: Creación de la Visualización

1. **Configuración de la Gráfica**: Se utilizó `matplotlib` para crear una gráfica de líneas que muestra la tendencia de los niveles de bacteriología y turbiedad a lo largo de los años.
2. **Etiquetado y Estilo**: Se añadieron títulos, etiquetas a los ejes y una leyenda para mejorar la claridad y comprensión de la gráfica.

## Preguntas que Puede Responder la Visualización

- **¿Cómo han variado los niveles de bacteriología en el agua de Chile desde 2019?**
  - Esta pregunta se puede responder observando la tendencia de la línea que representa los niveles de bacteriología.

- **¿Se ha mantenido constante la turbiedad del agua en Chile a lo largo de los años?**
  - La línea que muestra la turbiedad permite visualizar cualquier variación significativa en este indicador.

- **¿Hay correlación entre los niveles de bacteriología y turbiedad en los diferentes años?**
  - Comparando las dos líneas en la gráfica, se puede analizar si hay alguna relación entre ambos indicadores.

## Código Utilizado

Se ejecutó en Colab:

```python

import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV
file_path = r'/content/drive/MyDrive/Colab Notebooks/Base de datos combinada.csv'

# Cargar los datos
data = pd.read_csv(file_path)

# Extraer los años y convertirlos en enteros
data['Año'] = data['Año'].str.extract(r'(\d+)').astype(int)

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar los datos de Bacteriología y Turbiedad
ax.plot(data['Año'], data['Bacteriología'], label='Bacteriología', marker='o')
ax.plot(data['Año'], data['Turbiedad'], label='Turbiedad', marker='o')

# Añadir título y etiquetas de los ejes
ax.set_title('Tendencia de los niveles de Bacteriología y Turbiedad en Chile (2019-2023)')
ax.set_xlabel('Año')
ax.set_ylabel('Nivel')
ax.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()


