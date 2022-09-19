#import random
from random import randrange,choice

print(  list(range(10,20,2))    )


# Aleatoreos en un rango
print( randrange(20,50))
# Aleatoreos en un rango , el rango se crea con diferencia de 2 entre numeros
print( randrange(20,50,2))

mi_lista = [1,True,False,"Orca",{"key":"value"}]
print(choice(mi_lista))
print(choice(mi_lista))
print(choice(mi_lista))
print(choice(mi_lista))
print(choice(mi_lista))