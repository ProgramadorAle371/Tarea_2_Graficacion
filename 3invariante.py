import cv2
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import os

def calcular_momentos_invariantes(ruta_imagen, umbral=128):
    try:
        # 1. Cargar imagen correctamente
        imagen = Image.open(ruta_imagen).convert("L")  # Escala de grises
        imagen_np = np.array(imagen, dtype=np.uint8)  # ¡Importante: uint8!
        
        # 2. Binarización robusta
        _, imagen_binaria = cv2.threshold(imagen_np, umbral, 255, cv2.THRESH_BINARY)
        
        # Verificar si la imagen no está vacía
        if np.all(imagen_binaria == 0) or np.all(imagen_binaria == 255):
            raise ValueError("La imagen binaria no contiene objetos detectables.")
        
        # 3. Calcular momentos
        momentos = cv2.moments(imagen_binaria, binaryImage=True)
        
        if momentos["m00"] == 0:
            raise ValueError("No se detectaron objetos en la imagen (m00=0).")
        
        # 4. Calcular momentos invariantes
        resultados = []
        for p in range(3):
            for q in range(3):
                mu_pq = momentos.get(f"mu{p}{q}", 0.0)
                gamma = (p + q) / 2 + 1
                eta_pq = mu_pq / (momentos["m00"] ** gamma) if momentos["m00"] != 0 else 0.0
                
                resultados.append({
                    "p": p,
                    "q": q,
                    "η_pq": eta_pq
                })
        
        # Mostrar imagen binaria
        plt.imshow(imagen_binaria, cmap='gray')
        plt.title(f"Imagen Binaria: {os.path.basename(ruta_imagen)}")
        plt.show()
        
        # Retornar solo p, q y η_pq
        return pd.DataFrame(resultados, columns=["p", "q", "η_pq"])
    
    except Exception as e:
        print(f"Error procesando {ruta_imagen}: {e}")
        return None

# Procesar todas las imágenes en la carpeta
if __name__ == "__main__":
    carpeta = os.path.dirname(__file__)  # Carpeta actual
    extensiones_validas = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    
    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith(extensiones_validas):
            ruta = os.path.join(carpeta, archivo)
            print(f"\nProcesando: {archivo}")
            resultados = calcular_momentos_invariantes(ruta)
            
            if resultados is not None:
                print("\nResultados:")
                print(resultados.to_string(index=False))

# Cambiar la carpeta a "tarea 2"
if __name__ == "__main__":
    carpeta = os.path.join(os.path.dirname(__file__), "Tarea2")  # Carpeta "tarea 2"
    extensiones_validas = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    
    if os.path.exists(carpeta):
        for archivo in os.listdir(carpeta):
            if archivo.lower().endswith(extensiones_validas):
                ruta = os.path.join(carpeta, archivo)
                print(f"\nProcesando: {archivo}")
                resultados = calcular_momentos_invariantes(ruta)
                if resultados is not None:
                    print("\nResultados:")
                    print(resultados.to_string(index=False))
    else:
        print(f"La carpeta '{carpeta}' no existe.")