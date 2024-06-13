import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV
file_path = r'Entrega 4\Base de datos combinada.csv'  # Cambia esto a la ruta correcta de tu archivo CSV

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







