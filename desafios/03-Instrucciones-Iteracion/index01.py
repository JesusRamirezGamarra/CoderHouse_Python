"""
INSTRUCCIONES e ITERACCIÓN
Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:


1.	Mostrar una suma de los dos números
2.	Mostrar una resta de los dos números (el primero menos el segundo)
3.	Mostrar una multiplicación de los dos números
4.	Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
5.	En caso de no 
"""

option_menu = {
	1: 'Mostrar una suma de los dos números' , 
	2: 'Mostrar una resta de los dos números (el primero menos el segundo)',
	3: 'Mostrar una multiplicación de los dos números' ,
    4: 'Exit: Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará' ,
}

# This function will print out your option menu
def print_options():
	for key in option_menu.keys():
		print(key , '---' , option_menu[key])

def imput_value():
    try:
        Valor = float(input("Ingrese numero  :"))
        return Valor
    except ValueError:
        print("Error, no es un numero")
        return imput_value()

# Create your option functions here. / Add more for your needs
def option1(valorA, valorB):
    result = valorA + valorB
    print(f"La resta de los números : {valorA} y {valorB}, es igual a : {result}")
    print("................................................................")

def option2(valorA, valorB):
    result = valorA - valorB
    print(f"La suma de los números : {valorA} y {valorB}, es igual a : {result}")
    print("................................................................")	

def option3(valorA, valorB):
    result = valorA * valorB
    print(f"La suma de los números : {valorA} y {valorB}, es igual a : {result}")
    print("................................................................")	

if __name__ == '__main__':
    print_options()
    option = ""
    while(option not in option_menu.keys()) :
        option = int(input("Ingrese una opción: "))
        if(option == 4):
            break
        elif(option == 1):
            valorA = imput_value()
            valorB = imput_value()
            option1(valorA, valorB)
            print_options()
            option = ""
        elif(option == 2):
            valorA = imput_value()
            valorB = imput_value()
            option2(valorA, valorB)            
            print_options()
            option = ""
        elif(option == 3):
            valorA = imput_value()
            valorB = imput_value()
            option3(valorA, valorB)                        
            print_options()
            option = ""
        else:
            print("Opción no válida")
            print("................................")  
            print_options()
            option = ""
        
        