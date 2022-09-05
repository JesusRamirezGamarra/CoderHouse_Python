#3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
#Si el primer número es mayor que el segundo, debe devolver 1.
#Si el primer número es menor que el segundo, debe devolver -1.
#Si ambos números son iguales, debe devolver un 0.
#Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'



rd={'number01':int,'number':'integers',
    'number02':int,'number':'integers',
    'docstring':'relationship between 2 numbers to know if the first number is greater than, less than or equal to the second number.'}
def relacion(number01:'int',number02:'int')->rd:
    try:
        number01 = int(number01)
        number02 = int(number02)
        if type(number01)==int and type(number02)==int :
            if number01 > number02 :
                return 1
            elif number01 < number02 :
                return -1
            else :
                return 0
        else:
            #assert False,"parameter numero #01 o numero #02 no son numero enteros"
            return False
    except ValueError:
        print('Error, el parametro de numero #1 : {} y parametro numero #2 : {} no son numeros enteros, debe cambiarlos para continuar '.format(number01,number02))    
        # assert False,"Error, el parametro de numero #1 : {} o el parametro numero #2 : {} no son numeros enteros, debe cambiarlos para continuar ".format(number01,number02)
        return False



if __name__ == '__main__':
    assert relacion(5,10) == -1, 'ok'
    assert relacion(10,5) == 1, 'ok'
    assert relacion(5,5)  == 0, 'ok'
    assert relacion(5.0,'a')  == False, 'ok'
    
    
    print("*" * 100)
    print( relacion.__annotations__['return'] )    
    print( relacion(5,10)  )
    print( relacion(10,5)  )
    print( relacion(5,5)  )


    numero1 = input(f"Ingrese valor del numero #1 :")
    numero2 = input(f"Ingrese valor del numero #2 :")
    print(  relacion(numero1,numero2)  )
