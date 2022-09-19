class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    
    def hablar(self):
            print(f"miau , mi nombre es {self.nombre}")

mi_gata = Animal("Orca")
mi_otra_gata = Animal("Olivetta")

print(type(mi_gata))
print(type(mi_otra_gata))


mi_gata.hablar()
mi_otra_gata.hablar()

print(mi_gata.nombre)
print(mi_otra_gata.nombre)
