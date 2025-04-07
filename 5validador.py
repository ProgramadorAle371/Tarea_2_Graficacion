from PIL import Image, ImageSequence
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Cargar el GIF y convertir el primer cuadro a escala de grises
gif = Image.open("camellor.gif")
frames = [np.array(frame.convert("L")) for frame in ImageSequence.Iterator(gif)]

# Procesar solo el primer cuadro
imagen = frames[0]

# Dimensiones de la imagen
M, N = imagen.shape

# Aplicar Canny para detectar bordes en la imagen original
bordes_original = cv2.Canny(imagen, 100, 200)

# Trasladar la imagen 20 píxeles a la derecha y 20 píxeles abajo
M_translate = np.float32([[1, 0, 20], [0, 1, 20]])
imagen_trasladada = cv2.warpAffine(imagen, M_translate, (N, M))

# Aplicar Canny en la imagen trasladada
bordes_trasladados = cv2.Canny(imagen_trasladada, 100, 200)

# Calcular la diferencia entre la imagen original y la trasladada
diferencia = cv2.absdiff(imagen, imagen_trasladada)

# Mostrar imágenes
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.title("Imagen Original")
plt.imshow(imagen, cmap="gray")

plt.subplot(2, 2, 2)
plt.title("Imagen Trasladada")
plt.imshow(imagen_trasladada, cmap="gray")

plt.subplot(2, 2, 3)
plt.title("Bordes Originales")
plt.imshow(bordes_original, cmap="gray")

plt.subplot(2, 2, 4)
plt.title("Bordes Trasladados")
plt.imshow(bordes_trasladados, cmap="gray")

plt.show()
