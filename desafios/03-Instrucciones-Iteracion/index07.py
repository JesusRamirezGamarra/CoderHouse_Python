"""
INSTRUCCIONES e ITERACCIÓN
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:
"""

def compare_list_EqualElement(lista1, lista2):
    lista3 = []
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    return lista3

def compare_list_NotRepeatElement(lista):
    resultantList = []
    for element in lista:
        if element not in resultantList:
            resultantList.append(element)
    return resultantList

def compare_list_NotRepeatElementWithSet(lista):
    convert_list_to_set = set(lista)
    new_list = list(convert_list_to_set)

    return new_list

if __name__ == '__main__':
    lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
    lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
    lista_3 = compare_list_EqualElement(lista_1,lista_2)
    print ('Nueva Lista ( utilziando iteracion / FOR )  : ', compare_list_NotRepeatElement(lista_3) )
    print ('Nueva Lista ( utilziando SET )  : ',compare_list_NotRepeatElementWithSet(lista_3) )
    
