
# 1) Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura
# 🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

rd={'base':int,'units':'cm = centimeters',
    'height':int,'units':'cm = centimeters',
    'docstring':'If you want to calculate the area of ​​a space, do it by multiplying its length by its width. So you will get a certain amount of square meters. This is the standard procedure for calculating rectangles. For example: a room measures 30 meters by 15 meters.'}
def area_rectangulo(base:'int',height:'int')->rd:
    try:
        base = int(base)
        height = int(height)
        if type(base)==int and type(height)==int:
            return base * height
        else:
            return False
    except ValueError:
        print('Error, el parametro de base : {} o de altura {} no son numeros enteros, debe cambiarlos para continuar '.format(base,height))    
        return False



if __name__ == '__main__':
    assert area_rectangulo(15,10) == 150, 'ok'
    assert area_rectangulo(15.0,10.0) == 150 , 'ok'
    print("*" * 100)
    print( area_rectangulo.__annotations__['return'] )    
    print(  area_rectangulo(15,10)  )


    base = input(f"Ingrese valor de la base :")
    altura = input(f"Ingrese valor de la altura :")
    print(  area_rectangulo(base,altura)  )
