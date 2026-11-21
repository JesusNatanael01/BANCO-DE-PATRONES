# Banco de patrones - Genera en Python

# 1. PARÁMETROS
UMBRAL = 0.7  # 70% de parecido para considerar que es el patrón
TAMAÑO = 3    # Patrones de 3x3

# 2. BANCO DE PATRONES (como pequeñas imágenes)
# 1 = píxel negro, 0 = píxel blanco

banco_patrones = {
    "cruz": [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    "cuadrado": [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    "linea": [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
}

# 3. ALGORITMOS

def algoritmo_exacta(patron, imagen):
    # Algoritmo 1: Coincidencia exacta
    return patron == imagen

def algoritmo_distancia(patron, imagen):
    # Algoritmo 2: Distancia - cuenta cuántos píxeles son iguales 
    iguales = 0
    total = TAMAÑO * TAMAÑO
    for i in range(TAMAÑO):
        for j in range(TAMAÑO):
            if patron[i][j] == imagen[i][j]:
                iguales += 1
    return iguales / total

def algoritmo_similitud(patron, imagen):
    # Algoritmo 3: Similitud basada en porcentaje de coincidencia
    return algoritmo_distancia(patron, imagen)

# 4. FUNCIÓN PRINCIPAL - Buscar en el banco

def buscar_patron(imagen, algoritmo="similitud"):
    print(f"\nBuscando con algoritmo: {algoritmo}")
    for nombre, patron in banco_patrones.items():
        if algoritmo == "exacta":
            if algoritmo_exacta(patron, imagen):
                print(f"¡Encontrado! Es: {nombre}")
                return nombre
        elif algoritmo == "distancia":
            similitud = algoritmo_distancia(patron, imagen)
            print(f"{nombre}: distancia = {similitud:.2f}")
        elif algoritmo == "similitud":
            sim = algoritmo_similitud(patron, imagen)
            print(f"{nombre}: similitud = {sim:.2f}")
            if sim >= UMBRAL:
                print(f"¡Encontrado! Es: {nombre} con {sim*100:.1f}% de similitud")
                return nombre
    print("No se encontró patrón")
    return None

# 5. PRUEBA - Imagen a reconocer

imagen_prueba = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

# Probar los 3 algoritmos

buscar_patron(imagen_prueba, "exacta")
buscar_patron(imagen_prueba, "distancia")
buscar_patron(imagen_prueba, "similitud")
