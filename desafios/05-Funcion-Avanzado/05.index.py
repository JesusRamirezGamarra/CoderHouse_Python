# 5) Realizá una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10

rd={'numberToCut':int,'number':'integers',
    'lowerLimit':int,'number':'integers',
    'upperimit':int,'number':'integers',
    'docstring':'UPPER LIMIT AND LOWER LIMIT In mathematics, the upper limit and lower limit of a sequence are defined as the highest and lowest limit.'}
def recortar(numberToCut:'int',lowerLimit:'int',upperimit:'int')->rd:
    try:
        numberToCut = int(numberToCut)
        lowerLimit = int(lowerLimit)
        upperimit = int(upperimit)
        if type(numberToCut)==int and type(lowerLimit)==int and type(upperimit)==int :
            if (numberToCut < lowerLimit) :
                return lowerLimit
            elif (numberToCut > lowerLimit) :
                return upperimit
            else :
                return numberToCut
        else:
            # assert False,"parameter numero #01 o numero #02 no son numero enteros"
            return False
    except ValueError:
        print('Error, el número a recortar a recortar (parametro #01): {} , lowerLimit  (parametro #02): {} y upperimit  (parametro #03): : {} no son numeros enteros, debe cambiarlos para continuar '.format(numberToCut,lowerLimit,upperimit))    
        # assert False,"Error, el parametro de numero #1 : {} o el parametro numero #2 : {} no son numeros enteros, debe cambiarlos para continuar ".format(number01,number02)
        return False



if __name__ == '__main__':
    print('dsfdfdsf')
    recortar(15,0,10) 
    # print ( recortar(-12,24) ) 
    # assert recortar(15,0,10)  == 6, 'Prueba Satisfactoria parametros Numer01 :-12, Numer02 : 24'
    
    
    # print("*" * 100)
    # print( intermedio.__annotations__['return'] )    
    # print( intermedio(5,10)  )
    # print( intermedio(10,5)  )
    # print( intermedio(5,5)  )
    print ( recortar(15,0,10)   ) 

    # numberToCut = input(f"Ingrese valor a recortar :")
    # lowerLimit  = input(f"Ingrese valor del numero #1 para el Limite Inferior:")
    # upperimit   = input(f"Ingrese valor del numero #2 para el limite Superior:")
    # print(  recortar(numberToCut,lowerLimit,upperimit)  )
