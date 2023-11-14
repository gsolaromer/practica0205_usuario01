def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

# Ejemplo de uso:
numero = 5
resultado_recursivo = factorial_recursivo(numero)
print(f"El factorial de {numero} es: {resultado_recursivo}")