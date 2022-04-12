#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto (anio: int):
    return (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0))
        

print(bisiesto(2024))