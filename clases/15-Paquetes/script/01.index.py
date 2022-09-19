import sys
print(sys.argv)
#python 01.index.py mariano 1 True "[1,2,3]"

for argumento in sys.argv:
    print(type(argumento))
    print(argumento)

for indice,argumento in enumerate(sys.argv):
    print(f"el argumento nro {indice} es {argumento}")
    
