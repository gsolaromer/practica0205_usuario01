def calcular_media(muestra):
    """
    Calcula la media de una muestra de números.
    """
    if not muestra:
        return None  # Manejar el caso de una lista vacía para evitar divisiones por cero

    suma = sum(muestra)
    media = suma / len(muestra)
    return media

# Ejemplo de uso:
muestra_numeros = [5, 10, 15, 20, 25]
media_resultante = calcular_media(muestra_numeros)

print(f"La media de la muestra {muestra_numeros} es: {media_resultante}")