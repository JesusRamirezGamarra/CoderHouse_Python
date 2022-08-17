"""
INSTRUCCIONES e ITERACCIÓN
 Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
```
1). Todos los números del 0 al 10 [0, 1, 2, ..., 10]
2). Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
3). Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
4). Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
5). Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
```

🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))
numeros = [1, 3, 6, 9]
"""

if __name__ == '__main__':
    lista = list(range(0,11,1))
    print(f'1). Todos los números del 0 al 10 [0, 1, 2, ..., 10] : {lista}')
    lista = list(range(-10,1,1))
    print(f'2). Todos los números del -10 al 0 [-10, -9, -8, ..., 0] : {lista}')
    lista = list(range(0,21,2))
    print(f'3). Todos los números pares del 0 al 20 [0, 2, 4, ..., 20] : {lista}')
    print(f'Pero 0 no es un numero par, 0 es un numero neutro')
    lista.remove(0) # remove first occurance of x from list, Zero is not part of the list ,Zero is neutral number
    print(f'3). Todos los números pares del 0 al 20 [0, 2, 4, ..., 20] : {lista}')
    lista = list(range(-19,1,2))
    print(f'4). Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1] : {lista}')
    lista = list(range(0,51,5))
    print(f'5). Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50] : {lista}')