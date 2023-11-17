def saludar(nombre):
    """
    Saluda al usuario utilizando el nombre proporcionado.

    """
    return(f"¡Hola {nombre}!")
# Ejemplo de uso:
pregunta = input("¿Cómo se llama?")
nombre_usuario = pregunta
saludo = saludar(nombre_usuario)
print (saludo)