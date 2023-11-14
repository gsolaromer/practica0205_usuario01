import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    """
    area = math.pi * radio**2
    return area

def calcular_volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro dado su radio y altura.
    Utiliza la función calcular_area_circulo para obtener el área de la base.
    """
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen
# Ejemplo de uso:
radio_circulo = 3
altura_cilindro = 5

area_del_circulo = calcular_area_circulo(radio_circulo)
volumen_del_cilindro = calcular_volumen_cilindro(radio_circulo, altura_cilindro)

print(f"El área del círculo con radio {radio_circulo} es: {area_del_circulo}")
print(f"El volumen del cilindro con radio {radio_circulo} y altura {altura_cilindro} es: {volumen_del_cilindro}")