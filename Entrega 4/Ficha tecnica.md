# Ficha Técnica de la Base de Datos

## Características de los Datos

- **Nombre de la Base de Datos**: Base de datos combinada
- **Formato**: CSV 
- **Periodo de Tiempo**: 2019 - 2023
- **Cobertura Geográfica**: Chile
- **Fuente de Datos**: Datos combinados de distintas fuentes relacionadas con la calidad del agua en Chile

## Dimensiones de la Base de Datos

- **Número de Filas (Observaciones)**: 5 (cada fila representa un año)
- **Número de Columnas (Variables)**: 12

## Variables Incorporadas

| Variable                                   | Descripción                                                                 |
|--------------------------------------------|-----------------------------------------------------------------------------|
| `Año`                                      | Año del registro de datos (formato `ResultadoAño`)                          |
| `Mes`                                      | Mes del registro (en este caso, `Total Anual` para representar el año completo)|
| `Bacteriología`                            | Nivel de bacteriología en el agua                                           |
| `Turbiedad`                                | Nivel de turbiedad en el agua                                               |
| `Cloro Libre`                              | Nivel de cloro libre en el agua                                             |
| `Cloro Libre - Calidad`                    | Calidad del cloro libre en el agua                                          |
| `Parámetros Mensuales - Muestra`           | Muestra de parámetros mensuales                                             |
| `Parámetros Mensuales - Calidad`           | Calidad de parámetros mensuales                                             |
| `Parámetros Semestrales - Muestra`         | Muestra de parámetros semestrales                                           |
| `Parámetros Semestrales - Calidad`         | Calidad de parámetros semestrales                                           |
| `Control Mensual`                          | Control mensual de la calidad del agua                                      |
| `Control Semestral`                        | Control semestral de la calidad del agua                                    |


## Comentarios sobre la Base de Datos

La base de datos utilizada incluye registros anuales sobre varios parámetros de calidad del agua en Chile, desde 2019 hasta 2023. Cada registro anual proporciona valores agregados de diferentes indicadores como bacteriología, turbiedad, cloro libre, entre otros. La selección de los indicadores de bacteriología y turbiedad se basó en su relevancia para evaluar la calidad del agua potable.

## Procesamiento de la Base de Datos

- **Carga Inicial**: Los datos se cargaron en un DataFrame utilizando `pandas`.
- **Limpieza y Transformación**: Se extrajeron los años de las etiquetas de resultados y se convirtieron a formato entero. Se seleccionaron únicamente las columnas relevantes para la visualización.
- **Preparación para la Visualización**: Los datos procesados se utilizaron directamente para generar la gráfica de líneas.

## Selección de la Base de Datos

Esta base de datos fue seleccionada debido a su cobertura temporal adecuada y a la inclusión de indicadores críticos para evaluar la calidad del agua en Chile. La disponibilidad de datos anuales permite observar tendencias y variaciones a lo largo del tiempo, lo cual es esencial para el análisis y la visualización de la calidad del agua.

## Herramientas

- Python 3.x
- pandas
- matplotlib
