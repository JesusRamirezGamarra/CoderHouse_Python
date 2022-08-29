# El papa Gregorio XIII, asesorado por el astrónomo jesuita Christopher Clavius, el 24 de febrero de 1582 promulgó la bula Inter Gravissimas, en la que establecía que tras el jueves 4 de octubre de 1582 seguiría el viernes 15 de octubre de 1582.
# Con la eliminación de estos diez días desapareció el desfase con el año solar. Para que no volviera a ocurrir, en el nuevo calendario se eliminaron tres años bisiestos cada cuatro siglos. Con lo anterior, el 4 de octubre de 1582 fue el último día del calendario juliano y el 15 de octubre de 1582 constituyó el primer día del calendario gregoriano. Por tal razón no existieron las fechas del 5 al 14 de octubre de dicho año.
# Si se usan métodos actuales, el cálculo de fechas anteriores al 15 de octubre de 1582 siempre será erróneo, ya que se deben utilizar exclusivamente en retrospectiva hasta esta fecha y cambiar a cálculo de fechas julianas a partir del 4 de octubre de 1582, sin olvidar estos 10 días inexistentes.

rd={'type':int,'Year':'Only leap years','docstring':'Validate that the entered year is a leap year, > 1582'}
def año_bisiesto(year)->rd:
    try:
        year = int(year)
        if year >1581 :
            print( "El año {} es bisiesto".format(year) if not year % 4 and (year % 100 or  not year % 400) else "El año {} no es bisiesto".format(year))
        else : 
            print('Error, no es un año valido. "bis sextus dies ante calendas martii" fue instaurado el 24 de febrero de 1582 ( para mas informacion ver : https://es.wikipedia.org/wiki/A%C3%B1o_bisiesto ), Vuelva a ingresar un año Valido para continuar.')        

    except ValueError:
        print("Error, ingrese un número.No es un año valido. Vuelva a ingresar un año Valido para continuar.")

if __name__ == '__main__':
    year = input(f"Ingrese un año :")
    año_bisiesto(year)