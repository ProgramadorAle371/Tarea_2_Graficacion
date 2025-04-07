from PIL import Image
import numpy as np
import os

# Función para convertir la imagen a binaria
def convertir_a_binaria(imagen):
    imagen_grises = imagen.convert("L")
    imagen_binaria = np.array(imagen_grises) > 128
    return imagen_binaria

# Función para calcular el factor de escala necesario
def calcular_factor_escala(pixeles_objeto_original, pixeles_objeto_deseado):
    print("Pixeles deseados", pixeles_objeto_deseado)
    print("Pixeles originales", pixeles_objeto_original)
    return np.sqrt(pixeles_objeto_deseado / pixeles_objeto_original)

# Función para redimensionar la imagen
def redimensionar_imagen(imagen, factor_escala):
    nueva_anchura = int(imagen.width * factor_escala)
    nueva_altura = int(imagen.height * factor_escala)
    print("Factor de escala", factor_escala)
    print("Nueva altura", nueva_altura)
    print("Nueva anchura", nueva_anchura)
    print("Nuevo pixelado", nueva_anchura * nueva_altura)
    return imagen.resize((nueva_anchura, nueva_altura))

# Función principal
def transformar_imagen_gif(ruta_imagen, pixeles_objeto_deseado=500):
    imagen = Image.open(ruta_imagen)
    frames_transformados = []
    for frame in range(imagen.n_frames):
        imagen.seek(frame)
        imagen_binaria = convertir_a_binaria(imagen)
        pixeles_objeto_original = np.sum(imagen_binaria)
        factor_escala = calcular_factor_escala(pixeles_objeto_original, pixeles_objeto_deseado)
        imagen_redimensionada = redimensionar_imagen(imagen, factor_escala)
        frames_transformados.append(imagen_redimensionada)

    carpeta_destino = 'transformaciones'
    os.makedirs(carpeta_destino, exist_ok=True)
    nombre_salida = os.path.join(carpeta_destino, os.path.basename(ruta_imagen))
    frames_transformados[0].save(
        nombre_salida, save_all=True, append_images=frames_transformados[1:], loop=0
    )
    print(f"Imagen transformada guardada en '{nombre_salida}'.")

# Procesar todas las imágenes GIF en la carpeta actual
def procesar_carpeta_actual(pixeles_objeto_deseado=221280):
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    for archivo in os.listdir(carpeta_actual):
        if archivo.endswith('.gif'):
            ruta_imagen = os.path.join(carpeta_actual, archivo)
            print(f"Procesando: {ruta_imagen}")
            transformar_imagen_gif(ruta_imagen, pixeles_objeto_deseado)

# Usar la función con la carpeta actual
procesar_carpeta_actual()
