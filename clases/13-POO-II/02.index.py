# EJEMPLO 1
class Gata:
    
    patas = 4

    def __init__(self, nombre, madre):
        self.nombre = nombre
        self.madre = madre
        

    def mostrarse(self):
        print(self.nombre)
        print(self.patas)
        print(self.madre)
        print(type(self))


aceituna = Gata("Aceituna", "Manuela")
orca = Gata("Orca", "Una gata que no conocemos")


orca.mostrarse()
# Orca
# 4
# Una gata que no conocemos
# <class '__main__.Gata'>
aceituna.mostrarse()
# Aceituna
# 4
# Manuela
# <class '__main__.Gata'>