# https://docs.python.org/3/library/collections.html
#from collections import Counter
import collections


l = [1,2,3,4,1,2,3,1,2,1]
print(collections.Counter(l))
#print(Counter(l))

mi_palabra = "Avada Kadabra"
mi_contador = collections.Counter(mi_palabra)
print(mi_contador)
print(list(mi_contador.elements()))
print(list(mi_contador.most_common()))