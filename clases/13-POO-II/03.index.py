# Ejemplos
class Persona:

    reloj = "casio"
    sombra = True

    def __init__(self, nombre, segundo_nombre, pais):
        self.nombre = nombre
        self.segundo_nombre = segundo_nombre
        self.pais = pais


    def presentarse(self):
        print(f"Buenas noches, mi nombre es {self.nombre} {self.segundo_nombre} y estoy en {self.pais}")

    def cambiar_de_pais(self, pais):
        self.pais = pais


    def __str__(self):
        return f"Esta persona se llama {self.nombre}"

    def __len__(self):
        return 509

    def __getitem__(self, pos):
        return 1


persona_1 = Persona("Roberto", "Arnaldo", "Birmania")
persona_2 = Persona("Elena", "Silvia", "Latvia")

print(len(persona_1))
# 509
print(persona_1[0])
# 1
persona_1.presentarse()
# Buenas noches, mi nombre es Roberto Arnaldo y estoy en Birmania
persona_2.presentarse()
# Buenas noches, mi nombre es Elena Silvia y estoy en Latvia
persona_2.cambiar_de_pais("Argentina")
persona_2.presentarse()
# Buenas noches, mi nombre es Elena Silvia y estoy en Argentina






