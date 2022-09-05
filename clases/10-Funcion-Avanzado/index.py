

class Nabo:
    def __init__(self,
                    largo,
                    nombre,
                    color                 
                ):
            self.largo = largo
            self.nombre = nombre
            self.color = color

nabo = Nabo(12,"pepe","Rojo")
print(repr(nabo))
print(nabo.largo)
print(nabo.nombre)
print(nabo.color)



from dataclasses \
    import dataclass

@dataclass
class Nabo_:
    largo:int
    nombre:str
    color:str

nabo_ = Nabo_(12,"pepe","Rojo")
print(repr(nabo_))
print(nabo_.largo)
print(nabo_.nombre)
print(nabo_.color)
