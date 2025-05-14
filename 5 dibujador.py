import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Cargar imagen .gif (convertida a RGB)
nombre = "camellor.gif"
# Cargar la imagen
imagen = Image.open(nombre).convert("RGB")
img_array = np.array(imagen)

# Dimensiones
altura, ancho, _ = img_array.shape

# Crear figura con buena escala
fig, ax = plt.subplots(figsize=(ancho / 50, altura / 50), dpi=100)

# Mostrar imagen sin interpolación
ax.imshow(img_array, interpolation='none')

# Cuadrícula de 1 píxel
ax.set_xticks(np.arange(-0.5, ancho, 1), minor=True)
ax.set_yticks(np.arange(-0.5, altura, 1), minor=True)
ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)

# Ticks visibles cada cierto número de píxeles (ajustable)
intervalo_x = max(1, ancho // 20)
intervalo_y = max(1, altura // 20)
ax.set_xticks(np.arange(0, ancho, intervalo_x))
ax.set_yticks(np.arange(0, altura, intervalo_y))

# Estética de los ticks
plt.xticks(rotation=90, fontsize=6)
plt.yticks(fontsize=6)

# Título
ax.set_title("Gráfico de celdas negro/blanco con cuadrícula de "+nombre)

# Sin etiquetas de ejes
ax.set_xlabel("Ancho (pixeles)")
ax.set_ylabel("Alto (pixeles)")

# Mantener proporción exacta y ajustar el diseño
ax.set_aspect('equal')
plt.tight_layout()

# Mostrar ventana
plt.show()
