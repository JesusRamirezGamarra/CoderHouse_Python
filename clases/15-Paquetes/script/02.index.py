import sys
print(sys.argv)
#python 01.index.py mariano 1 True "[1,2,3]"

# if len(sys.argv) == 3:
#     texto = sys.argv[1]
#     repeticiones = int(sys.argv[2])
#     for r in range(repeticiones):
#         print(texto)
# else:
#     print("Error - Introduce los argumentos corectamente")
#     print('Ejemplo - escribir 02.index.py "Texto" 5')


def imprimir_suma(a,b):
    print(a+b)
    
if len(sys.argv) == 3:    
    mi_numero = int(sys.argv[1])
    mi_otro_numero = int(sys.argv[2])
    imprimir_suma(mi_numero,mi_otro_numero)
else :
    print("Error - Introduce los argumentos corectamente, se requieren 2 argumentos")
    print("Ejemplo - escribir 02.index.py 1 5")
