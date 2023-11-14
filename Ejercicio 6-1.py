def decimal_a_binario(decimal):
    """
    Convierte un número decimal a binario.

    Parameters:
    decimal (int): Número decimal a convertir.

    Returns:
    str: Representación binaria del número decimal.
    """
    return bin(decimal)[2:]

# Ejemplo de uso:
numero_decimal = 15
binario_resultante = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es: {binario_resultante}")