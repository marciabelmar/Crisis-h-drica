






## Procesamiento de datos de caudales medios del río Itata
Este paso del proyecto detalla el proceso para transformar los datos en bruto de los caudales medios mensuales del Río Itata en datos limpios y agregados por año, excluyendo el año 2023, que no tiene los datos completos. Los datos se consolidan en un archivo CSV y XLSX con las columnas "Año" y "Caudal (m3/s)".
Los datos brutos fueron obtenidos de la Dirección General de Aguas (DGA), quienes tienen datos según la estación de medición, es por ello que decidí combinar todos estos datos para obtener un panorama general de los datos del caudal del río Itata a través de los años. 
En un comienzo estaba considerado el año 2023 entre los años de análisis, pero se puede observar que después de las inundaciones por los sistemas frontales que afectaron a la región en julio y agosto, varias de las estaciones no arrojaron información, lo que podría resultar engañoso.

### Estructura del proyecto
Caudales-medios-mensuales-Rio-Itata.xlsx: Archivo Excel con los datos en bruto de los caudales medios mensuales.
process_data.py: Script de Python para procesar los datos.

### Pasos para pocesar los datos
1. Montar Google Drive

python
from google.colab import drive
drive.mount('/content/drive')

2. Cargar el archivo excel

python
import pandas as pd

file_path = '/content/drive/MyDrive/nav/Caudales-medios-mensuales-Rio-Itata.xlsx'
excel = pd.ExcelFile(file_path)
sheets = excel.sheet_names
dfs = [excel.parse(sheet) for sheet in sheets]

3. Inicializar el diccionario para almacenar los datos anuales

python
yearly_data = {
    2019: 0,
    2020: 0,
    2021: 0,
    2022: 0
}

4. Definir las columnas de datos mensuales

python
month_columns = ['Unnamed: 3', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 9', 
                 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 
                 'Unnamed: 16', 'Unnamed: 17']

5. Sumar los datos mensuales por año

python
def sum_monthly_data(df):
    df_filtered = df.dropna(how='all').reset_index(drop=True)
    
    if df_filtered.shape[0] > 1:
        for index, row in df_filtered.iterrows():
            if row['GOBIERNO DE CHILE'] in [2019, 2020, 2021, 2022]:
                year = row['GOBIERNO DE CHILE']
                monthly_values = pd.to_numeric(row[month_columns], errors='coerce')  # Convertir a numérico, forzando errores a NaN
                yearly_sum = monthly_values.sum(skipna=True)  # Sumar los valores numéricos, ignorando NaNs
                yearly_data[year] += yearly_sum

for df in dfs:
    sum_monthly_data(df)

6. Convertir los resultados a un DataFrame
Convertimos los resultados del diccionario a un DataFrame para su visualización y guardado.

python
yearly_data_df = pd.DataFrame.from_dict(yearly_data, orient='index', columns=['Caudal (m3/s)'])
yearly_data_df.index.name = 'Año'
title = "Caudales Medios Anuales Río Itata (m3/s)"
yearly_data_df.columns.name = title

7. Guardar los resultados en archivos CSV y XLSX

python
csv_file_path = '/content/drive/MyDrive/nav/Yearly_Data_Summary.csv'
yearly_data_df.to_csv(csv_file_path, index_label='Año')

xlsx_file_path = '/content/drive/MyDrive/nav/Yearly_Data_Summary.xlsx'
with pd.ExcelWriter(xlsx_file_path) as writer:
    yearly_data_df.to_excel(writer, index_label='Año', sheet_name='Resumen')

print(f'Resultados guardados en {csv_file_path} y {xlsx_file_path}')
Resultados
Yearly_Data_Summary.csv: Contiene los datos anuales de caudales medios del Río Itata en formato CSV.
Yearly_Data_Summary.xlsx: Contiene los datos anuales de caudales medios del Río Itata en formato XLSX.

### Los datos
Los datos en ambos archivos tienen las siguientes columnas:

Año: El año correspondiente.
Caudal (m3/s): El caudal medio anual en metros cúbicos por segundo.

## Creación de la visualización interactiva de la variación de los caudales del río Itata
Se utilizaron los datos del archivo Excel, generado en el paso anterior, y la biblioteca Plotly en Google Colab.


## Pasos para crear la visualización

1. Montar Google Drive

python
from google.colab import drive
drive.mount('/content/drive')

2. Cargar el Archivo Excel

python
import pandas as pd
import plotly.express as px

3. Leer el archivo Excel
df = pd.read_excel(file_path, sheet_name='Resumen')

4. Asegurarse de que los años sean enteros
df['Año'] = df['Año'].astype(int)

5. Definir una nueva paleta de colores acorde al manual de marca nuevo
new_color_palette = ["#0026AE", "#0EBCCD", "#BCD5FF"]

6. Crear un gráfico de área interactivo con los nuevos colores
fig_area_corrected = px.area(df, x='Año', y='Caudal (m3/s)', title='Variación de los caudales del río Itata a través de los años',
                             labels={'Año': 'Año', 'Caudal (m3/s)': 'Caudal (m3/s)'},
                             color_discrete_sequence=new_color_palette)

7. Configurar los ticks del eje x para mostrar solo los años relevantes
fig_area_corrected.update_layout(xaxis=dict(tickmode='array', tickvals=[2019, 2020, 2021, 2022]))

8. Guardar el gráfico en un archivo HTML
fig_area_corrected.write_html('variacion_caudales_rio_itata_area_corrected.html')

9. Mostrar el gráfico
fig_area_corrected.show()

10. Ejecutar el código y descargar el archivo

El código generará un archivo HTML llamado variacion_caudales_rio_itata_area_corrected.html que contendrá la visualización interactiva.

## Manual de marca
1. Tipografía: Para la audiencia definida, es importante elegir tipografías que sean legibles y accesibles, adecuadas tanto para la lectura como para la presentación de información clara y concisa. A continuación, dos tipografías compatibles con Google Fonts que se ajustan al perfil de la audiencia:

### Roboto:
Tipografía sans-serif moderna y muy legible. Es ideal para contenido digital y es ampliamente utilizada en interfaces de usuario, lo que la hace familiar para personas que consumen contenido en línea.
Uso: Textos largos, párrafos de información.
2. Montserrat
Montserrat es otra tipografía sans-serif que combina un estilo moderno con una excelente legibilidad. Sus formas geométricas son atractivas y fáciles de leer, lo que la hace adecuada para títulos y subtítulos, así como para párrafos de texto.
Uso: Títulos, subtítulos, y elementos destacados de la web story.

