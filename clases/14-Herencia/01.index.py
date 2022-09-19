class Animal:
    def __init__(self, especie, edad):  # Constructor como siempre en la clase Padre
        self.especie = especie
        self.edad = edad

    def hablar(self):  # Método generico vacio por ahora
        pass

    def moverse(self):  # Método generico vacio por ahora
        pass

    def __str__(self):
        return f"ESPECIE: {self.especie} , EDAD: {self.edad}"

    def describir(self):  # Método con una implementación
        print(f"Soy un animal del tipo: {type(self)}")
        # print(f"Soy un animal del tipo: {type(self).__name__}")


class Perro(Animal):
    def hablar(self):
        print(f"barf barf !!!")


class Gata(Animal):
    def hablar(self):
        print(f"miau miau !!!")


class Escarabajo(Animal):
    def hablar(self):
        print(f"CrcrrrcRrrCr")

    def Picar(self):
        print(f"PicaPica")


mi_perro = Perro("mamifero", "Dishy")
mi_gata = Gata("mamifero", "peluza")
mi_escarabajo = Escarabajo("insecto", "x")


mi_perro.describir()
mi_gata.describir()
mi_escarabajo.describir()


mi_perro.hablar()
mi_gata.hablar()
mi_escarabajo.hablar()

# mi_perro.Picar()       # AttributeError: 'Perro' object has no attribute 'Picar'
# mi_gata.Picar()         # AttributeError: 'Gata' object has no attribute 'Picar'
mi_escarabajo.Picar()
