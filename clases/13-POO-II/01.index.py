# mi_lista = list()
# mi_lista.append(6)

# print(type(mi_lista))
# print(mi_lista)



class Gata:
    # pass

    def __init__(self,nombre):
        self.nombre = nombre
        self.patas = 4


Orca = Gata("Orca")
Aceituna = Gata("Aceituna")

print(Orca.nombre)
print(type(Orca))
print(Aceituna.nombre)
print(type(Aceituna))


print(Aceituna.patas)