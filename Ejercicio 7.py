def contar_frecuencia_palabras(fragmento_texto):
    """
    Cuenta la frecuencia de cada palabra en un fragmento de texto.

    Parameters:
    fragmento_texto (str): Fragmento de texto.

    Returns:
    dict: Diccionario con las palabras y sus frecuencias.
    """
    palabras = fragmento_texto.split()
    frecuencia_palabras = {}

    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    return frecuencia_palabras

def palabra_mas_repetida_y_frecuencia(diccionario_frecuencias):
    """
    Encuentra la palabra más repetida y su frecuencia en un diccionario de frecuencias.

    Parameters:
    diccionario_frecuencias (dict): Diccionario con palabras y sus frecuencias.

    Returns:
    tuple: Tupla con la palabra más repetida y su frecuencia.
    """
    palabra_mas_repetida, frecuencia = max(diccionario_frecuencias.items(), key=lambda x: x[1])
    return palabra_mas_repetida, frecuencia

# Ejemplo de uso:
texto_ejemplo = "Este es un ejemplo de texto. Este texto tiene palabras. Palabras repetidas tienen frecuencia."

# Contar la frecuencia de las palabras
diccionario_frecuencias = contar_frecuencia_palabras(texto_ejemplo)
print("Diccionario de frecuencias:", diccionario_frecuencias)

# Encontrar la palabra más repetida y su frecuencia
palabra_repetida, frecuencia_repetida = palabra_mas_repetida_y_frecuencia(diccionario_frecuencias)
print(f"La palabra más repetida es '{palabra_repetida}' con frecuencia {frecuencia_repetida}.")