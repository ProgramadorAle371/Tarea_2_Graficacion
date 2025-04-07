from PIL import Image
import numpy as np

# Cargar la imagen
imagen = Image.open('t1.gif')

# Convertir a escala de grises si no está en ella
imagen_grises = imagen.convert("L")

# Convertir la imagen a un array numpy
imagen_array = np.array(imagen_grises)

# Definir un umbral para convertir la imagen a binaria (0 = fondo, 1 = objeto)
umbral = 128

# Convertir a binario: 1 para píxeles mayores que el umbral, 0 para píxeles menores
imagen_binaria = imagen_array > umbral

# Calcular la cantidad de píxeles con valor 1 (objetos)
pixeles_objeto = np.sum(imagen_binaria)

# Calcular la cantidad de píxeles con valor 0 (fondo)
pixeles_fondo = imagen_array.size - pixeles_objeto

# Mostrar resultados
print(f'Cantidad total de píxeles: {imagen_array.size}')
print(f'Cantidad de píxeles de valor 1 (objetos): {pixeles_objeto}')
print(f'Cantidad de píxeles de valor 0 (fondo): {pixeles_fondo}')
