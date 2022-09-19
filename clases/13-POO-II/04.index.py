class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    def presentarse(self):
        return f"Hola, me llamo {self.nombre}"

    
class Gata:

    def __init__(self, nombre, humano):
        self.nombre = nombre
        self.humano = humano

    
    def presentarse(self):
        print(f"Miau! soy {self.nombre} y vivo con mi humane que se va a presentar ahora:\n {self.humano.presentarse()} ")


mi_hermana = Persona("Soledad")
orca = Gata("Orca", mi_hermana)

orca.presentarse()
# Miau! soy Orca y vivo con mi humane que se va a presentar ahora:
# Hola, me llamo Soledad 
