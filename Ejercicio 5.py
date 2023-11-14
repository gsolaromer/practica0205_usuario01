def cuadrados_de_muestra(muestra):
    """
    Devuelve una lista con los valores al cuadrado de la muestra dada.
    """
    return [x**2 for x in muestra]

# Ejemplo de uso:
muestra_numeros = [2, 4, 6, 8, 10]
cuadrados_resultantes = cuadrados_de_muestra(muestra_numeros)

print(f"La muestra original es: {muestra_numeros}")
print(f"Los cuadrados de la muestra son: {cuadrados_resultantes}")