import math

def calcular_entropia(datos):
    conteo = {c: datos.count(c) for c in set(datos)}
    return -sum((f/len(datos)) * math.log2(f/len(datos)) for f in conteo.values())

def leer_datos(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    datos = leer_datos('cancion.txt')
    vocales = 'aeiouAEIOU'
    datos_vocales = [c for c in datos if c in vocales]
    datos_consonantes = [c for c in datos if c.isalpha() and c not in vocales]
    print(f"Entropía de vocales: {calcular_entropia(datos_vocales):.4f}")
    print(f"Entropía de consonantes: {calcular_entropia(datos_consonantes):.4f}")

if __name__ == "__main__":
    main()
