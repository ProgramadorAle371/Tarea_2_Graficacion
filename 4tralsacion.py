from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cargar imagen GIF
gif_path = "camellor.gif"
gif = Image.open(gif_path)

# Procesar el primer fotograma del GIF
frame = gif.convert("L")  # Convertir a escala de grises
imagen = np.array(frame)

# Dimensiones de la imagen
M, N = imagen.shape

# Calcular centroides
y_indices, x_indices = np.indices((M, N))
m00 = np.sum(imagen)
x_cm = np.sum(x_indices * imagen) / m00
y_cm = np.sum(y_indices * imagen) / m00

# Trasladar la imagen a una nueva posición (ejemplo: desplazar 10 píxeles en x e y)
M_translate = np.float32([[1, 0, 10], [0, 1, 10]])
imagen_trasladada = np.zeros_like(imagen)
for y in range(M):
    for x in range(N):
        new_x = x + 10
        new_y = y + 10
        if 0 <= new_x < N and 0 <= new_y < M:
            imagen_trasladada[new_y, new_x] = imagen[y, x]

# Calcular los momentos centrales
momentos = {}
for p in range(3):
    for q in range(3):
        if p == 0 and q == 0:
            continue  # μ_00 no es informativo
        momento = np.sum(((x_indices - x_cm) ** p) * ((y_indices - y_cm) ** q) * imagen)
        momentos[(p, q)] = momento

# Crear una tabla con los resultados
tabla_resultados = pd.DataFrame(momentos.items(), columns=["(p, q)", "Momento Central"])
print(tabla_resultados)

# Mostrar imágenes original y trasladada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(imagen, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Imagen Trasladada")
plt.imshow(imagen_trasladada, cmap='gray')

plt.show()
