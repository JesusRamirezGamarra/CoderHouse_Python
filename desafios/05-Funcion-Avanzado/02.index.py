#2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio
#🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes 
#utilizar el valor 3.14159 como pi o importarlo del módulo math.
#Por ejemplo:
#```
#import math
#print(math.pi)
#```

import math

rd={'radio':int,'units':'cm = centimeters',
    'docstring':'The area of ​​a circle is pi multiplied by the radius squared (A = π r²).'}
def area_circulo(radio:'int')->rd:
    try:
        radio = int(radio)
        if type(radio)==int :
            return   round((math.pi * (radio ** 2) ),4)
        else:
            return False
    except ValueError:
        print('Error, el parametro de radio : {}  no son numeros enteros, debe cambiarlos para continuar '.format(radio))    
        return False



if __name__ == '__main__':
    assert area_circulo(5) == 78.5398, 'ok'
    assert area_circulo(5.0) == 78.5398 , 'ok'
    print("*" * 100)
    print( area_circulo.__annotations__['return'] )    
    print(  area_circulo(5)  )


    radio = input(f"Ingrese valor del radio :")
    print(  area_circulo(radio)  )
