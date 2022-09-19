import collections
Fish = collections.namedtuple("Fish",["name","species","tank"])
print(Fish) # genera una clase x eso colocamos el nombre de variable en Mayus
print(type(Fish))

mi_pececito = Fish("Nemo","pez payaso",None)
print(type(mi_pececito))
print(mi_pececito.name)
print(mi_pececito[0])

mi_dict = mi_pececito._asdict()
print(type(mi_dict))
print(mi_dict)