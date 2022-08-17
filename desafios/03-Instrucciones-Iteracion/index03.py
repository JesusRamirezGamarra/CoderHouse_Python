"""
INSTRUCCIONES e ITERACCIÓN
Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

🖐 Ayuda: Podes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

"""

if __name__ == '__main__':
    suma = 0
    for i in range(1, 101, 2):
        suma += i
    print(f'La suma de los números impares desde el 0 hasta el 100 es: {suma}')

    suma = sum(list(range(1,101,2)))
    print(f'La suma de los números impares desde el 0 hasta el 100 es: {suma}')    