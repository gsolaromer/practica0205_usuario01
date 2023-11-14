def binario_a_decimal(binario):
    """
    Convierte un número binario a decimal.

    Parameters:
    binario (str): Representación binaria a convertir.

    Returns:
    int: Número decimal resultante.
    """
    return int(binario, 2)

# Ejemplo de uso:
numero_binario = "1101"
decimal_resultante = binario_a_decimal(numero_binario)
print(f"El número binario {numero_binario} en decimal es: {decimal_resultante}")