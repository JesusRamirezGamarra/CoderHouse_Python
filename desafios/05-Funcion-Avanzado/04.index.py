# 4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:
# 🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

# Comprueba el punto intermedio entre -12 y 24


rd={'number01':int,'number':'integers',
    'number02':int,'number':'integers',
    'docstring':'The midpoint between two points is a point that has coordinates that lie exactly midway between the two points. These coordinates can be found by adding the x-coordinates of the two points and dividing by 2.'}
def intermedio(number01:'int',number02:'int')->rd:
    try:
        number01 = int(number01)
        number02 = int(number02)
        if type(number01)==int and type(number02)==int :
            # assert True,"Calculo de punto medio satisfactorio"
            return ( number01 + number02 ) / 2
        else:
            # assert False,"parameter numero #01 o numero #02 no son numero enteros"
            return False
    except ValueError:
        print('Error, el parametro de numero #1 : {} y parametro numero #2 : {} no son numeros enteros, debe cambiarlos para continuar '.format(number01,number02))    
        # assert False,"Error, el parametro de numero #1 : {} o el parametro numero #2 : {} no son numeros enteros, debe cambiarlos para continuar ".format(number01,number02)
        return False



if __name__ == '__main__':
    #print ( intermedio(-12,24) ) 
    assert intermedio(-12,24)  == 6, 'Prueba Satisfactoria parametros Numer01 :-12, Numer02 : 24'
    
    
    # print("*" * 100)
    # print( intermedio.__annotations__['return'] )    
    # print( intermedio(5,10)  )
    # print( intermedio(10,5)  )
    # print( intermedio(5,5)  )
    print ( intermedio(-12,24) ) 

    numero1 = input(f"Ingrese valor del numero #1 :")
    numero2 = input(f"Ingrese valor del numero #2 :")
    print(  intermedio(numero1,numero2)  )
