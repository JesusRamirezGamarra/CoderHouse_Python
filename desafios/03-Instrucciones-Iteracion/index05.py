"""
INSTRUCCIONES e ITERACCIÓN
Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

numeros = [1, 3, 6, 9]
"""

def imput_NroDato():
    try:
        
        value = int(input(f"Ingrese un numero entero del 0 al 9 : "))
        if(value in range(0,10,1)):
            return value
        else :
            print("Error, no es un numero entero del 0 al 9")
            return imput_NroDato()
    except ValueError:
        print("Error, no es un numero")
        return imput_NroDato()




if __name__ == '__main__':
    numeros = [1, 3, 6, 9]
    value = imput_NroDato()

    if value in numeros :
        print(f'El numero {value} se encuentra en la lista')
    else :
        print(f'El numero {value} NO se encuentra en la lista')
    print("................................................................")
