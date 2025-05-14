import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage import measure

# Cargar imagen .gif (convertida a RGB)
nombre = "camellor.gif"
# Cargar la imagen
imagen = Image.open(nombre).convert("RGB")
img_array = np.array(imagen)

# Convertir la imagen a blanco y negro (usando un umbral para identificar los píxeles blancos)
umbral = 200
blanco = np.all(img_array >= umbral, axis=-1)  # Identificar píxeles blancos

# Convertir la imagen a escala de grises para mostrar los píxeles grises
grises = np.zeros_like(blanco, dtype=float)
grises[blanco] = 0.9  # Hacer los píxeles blancos grises (valor más bajo)
grises[~blanco] = 0.1  # Hacer los píxeles negros más oscuros (valor más bajo)

# Detectar los contornos de la imagen binarizada con la libreria
contornos = measure.find_contours(grises, level=0.5)

# Dimensiones de la imagen
altura, ancho = grises.shape

# Crear figura con buena escala
fig, ax = plt.subplots(figsize=(ancho / 50, altura / 50), dpi=100)

# Mostrar la imagen con los píxeles grises
ax.imshow(grises, cmap='gray', interpolation='none', vmin=0.1, vmax=0.9)

# Dibuja los contornos con líneas rojas
for contorno in contornos:
    ax.plot(contorno[:, 1], contorno[:, 0], color='red', lw=2)

# Cuadrícula de 1 píxel
ax.set_xticks(np.arange(-0.5, ancho, 1), minor=True)
ax.set_yticks(np.arange(-0.5, altura, 1), minor=True)
ax.grid(which='minor', color='lightgray', linestyle='-', linewidth=0.5)

# Ticks visibles cada cierto número de píxeles (ajustable)
intervalo_x = max(1, ancho // 20)
intervalo_y = max(1, altura // 20)
ax.set_xticks(np.arange(0, ancho, intervalo_x))
ax.set_yticks(np.arange(0, altura, intervalo_y))

# Estética de los ticks
plt.xticks(rotation=90, fontsize=6)
plt.yticks(fontsize=6)

# Título
ax.set_title("Contorno en rojo de "+nombre)

# Sin etiquetas de ejes
ax.set_xlabel("Ancho (pixeles)")
ax.set_ylabel("Alto (pixeles)")

# Mantener proporción exacta y ajustar el diseño
ax.set_aspect('equal')
plt.tight_layout()

# Mostrar ventana
plt.show()
