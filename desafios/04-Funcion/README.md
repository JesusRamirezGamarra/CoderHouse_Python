
<p align="center">
  <p align="center">    
    <img src="https://github.com/JesusRamirezGamarra/CoderHouse_ReactJS/blob/Desafio-07/public/images/Logo_Negro.png" alt="BFFs" height="250">    
  </p>
  <p align="center">
       CoderHouse - Phython
  </p>
</p>

# INSTRUCCIONES 
Realizar una funcion llamada año_bisiesto:

1. Recibirá un año por parámetro
2. Imprimirá "El año año es bisiesto" si el año es bisiesto
3. Imprimirá "El año año no es bisiesto" si el año no es bisiesto
4. Si se ingresa algo que no sea número debe indicar que se ingrese un número.


# >>Información a tener en cuenta al realizar el entregable:
 
Se recuerda que los años bisiestos son múltiplos de 4. pero los múltiplos de 100 no lo son, aunque los
múltiplos de 400 sí, Estos son algunos ejemplos de posibles respuestas: 
* 2012 es bisiesto 
* 2010 no es bisiesto 
* 2000 es bisiesto
* 1900 no es bisiesto.


## Nota : 
### Reforma gregoriana
#### Artículo principal: Calendario gregoriano
El papa Gregorio XIII, asesorado por el astrónomo jesuita Christopher Clavius, el 24 de febrero de 1582 promulgó la bula Inter Gravissimas, en la que establecía que tras el jueves 4 de octubre de 1582 seguiría el viernes 15 de octubre de 1582.

Con la eliminación de estos diez días desapareció el desfase con el año solar. Para que no volviera a ocurrir, en el nuevo calendario se eliminaron tres años bisiestos cada cuatro siglos. Con lo anterior, el 4 de octubre de 1582 fue el último día del calendario juliano y el 15 de octubre de 1582 constituyó el primer día del calendario gregoriano. Por tal razón no existieron las fechas del 5 al 14 de octubre de dicho año.

Si se usan métodos actuales, el cálculo de fechas anteriores al 15 de octubre de 1582 siempre será erróneo, ya que se deben utilizar exclusivamente en retrospectiva hasta esta fecha y cambiar a cálculo de fechas julianas a partir del 4 de octubre de 1582, sin olvidar estos 10 días inexistentes.

## Algoritmo computacional
Un año es bisiesto si es:

* Divisible entre 4.
* No divisible entre 100.
* Divisible entre 400. (2000 y 2400 son bisiestos pues aún siendo divisibles entre 100 lo son también entre 400. Pero los años 1900, 2100, 2200 y 2300 no lo son porque sólo son divisibles entre 100).

Desde un enfoque algorítmico, se consideran las proposiciones o enunciados lógicos siguientes:

* p: Es divisible entre 4
* q: Es divisible entre 100 (¬q entonces significa no divisible entre 100)
* r: Es divisible entre 400
  
Entonces se utiliza la fórmula lógica ```p^(¬q V r )``` para establecer si un año dado es bisiesto: es bisiesto si es divisible entre cuatro y (no es divisible entre 100 o es divisible entre 400).