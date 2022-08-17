"""
INSTRUCCIONES e ITERACCIÓN
Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
"""

if __name__ == '__main__':
    continuar = True
    while continuar:
        try:
            numero = int(input('Ingrese un numero impar: '))
            if numero % 2 == 0:
                print('Por favor Ingresar un numero impar')
            else:
                continuar = False
                print(f'El numero ingresado es {numero}')
                break
        except ValueError:
            print('Por favor Ingresar un numero impar')
            continue
        except KeyboardInterrupt:
            print('Saliendo del programa')
            break
        finally:
            if(continuar == False):
                print('Saliendo del programa')
                break