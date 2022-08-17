"""
INSTRUCCIONES e ITERACCIÓN
Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:

"""

def imput_NroDato():
    try:
        Valor = int(input(f"Ingrese la cantidad de datos a ingresar : "))
        return Valor
    except ValueError:
        print("Error, no es un numero")
        return imput_NroDato()

def imput_value(i):
    try:
        Valor = float(input(f"Ingrese numero {i} :"))
        return Valor
    except ValueError:
        print("Error, no es un numero")
        return imput_value(i)



if __name__ == '__main__':
    sumaDato = 0
    CantidadDato = 0
    CantidadDato = imput_NroDato()

    for i in range(CantidadDato):
        sumaDato += imput_value(i+1)
    print(f'La media aritmética de los datos es : {sumaDato / CantidadDato}')
    print("................................................................")
