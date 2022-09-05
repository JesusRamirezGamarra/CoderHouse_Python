# 6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:
# 🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()
# Por ejemplo:
# ```
# pares, impares = separar([6,5,2,1,7])
# print(pares)   # valdría [2, 6]
# print(impares)  # valdría [1, 5, 7]

# ```


rd={'listNumber':list,'list number':'integers',
    'docstring':'odd and even list'}
def separar(listNumber:'list')->rd:
    try:
        if  listNumber and type(listNumber)==list :
            if( all(map(  lambda p: str(p).isdigit(),listNumber))   ):
                list_odd = [numero for numero in listNumber if numero %2 == 1]
                list_even = [numero for numero in listNumber if numero %2 == 0]
                return [sorted(list_even),sorted(list_odd)]
            else : 
                print('Error, el parametro #1 listNumber: {} , contiene elmentos no numericos, debe modificarla para poder continuar '.format(listNumber))    
                return False            
        else:
            print('Error, el parametro #1 listNumber: {} , no es una lista '.format(listNumber))    
            return False
    except ValueError:
        print('Error, el parametro #1 listNumber: {} , contiene elmentos no numericos, debe modificarla para poder continuar '.format(listNumber))    
        return False

if __name__ == '__main__':
    assert separar([1, 5, 7, 13, 22, 15, 26, 64, 34, 72, 52, 14])  == [[14, 22, 26, 34, 52, 64, 72],[1, 5, 7, 13, 15]], 'Ok'
    assert separar(['a', 5, 7, 13, 22, 15, 26, 64, 34, 72, 52, 14])  == False, 'Ok'
    print("*" * 100)
    print( separar.__annotations__['return'] )    
    pares, impares = separar([1, 5, 7, 13, 22, 15, 26, 64, 34, 72, 52, 14])  
    print(pares)
    print(impares)