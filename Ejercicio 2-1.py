def factorial_bucle(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
# Ejemplo de uso:
numero = 5
resultado_bucle = factorial_bucle(numero)
print(f"El factorial de {numero} es: {resultado_bucle}")