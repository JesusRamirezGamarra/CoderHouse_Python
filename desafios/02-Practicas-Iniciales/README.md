
<p align="center">
  <p align="center">    
    <img src="https://github.com/JesusRamirezGamarra/CoderHouse_ReactJS/blob/Desafio-07/public/images/Logo_Negro.png" alt="BFFs" height="250">    
  </p>
  <p align="center">
       CoderHouse - Phython
  </p>
</p>

# PRACTICAS INICIALES

## Consigna 1:  
### Identifica el tipo de dato (int, float, string, list o touple) de los siguientes valores literales:

```
Dato : 
1)  "Hola Mundo" 
2)  [1, 10, 100]
3)  -25
4)  (8, 100, -12)
5)  1.167
6)  ["Hola", "Mundo"]
7)  ' '
8)  (1, -5, "Hola!")
```
* nota_1 cuenta como el 40% de la nota final
* nota_2 cuenta como el 60% de la nota final

## Consigna 2:  
### Determina mentalmente (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables:

```
a = 10
b = -5
c = "Hola"
d = [1, 2, 3]
e= (4,5,6)
```

```
Ejecutar
1 ) print(a * 5)  
2)  print(a - b)    
3)  print(c + "Mundo") 
4)  print(c * 2)        
5)  print(c[-1])        
6)  print(c[1:])    
7)  print(d + d)       
8)  print(e[1])
9)  print(e+(7,8,9))

```

## Consigna 3:  
### El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

```
In [1]:
numero_1 = 9
numero_2 = 3
numero_3 = 6
​
media = numero_1 + numero_2 + numero_3 / 3
print("La nota media es", media)
La nota media es 14.0

```

## Consigna 4:  
### A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media. Cada nota tiene un valor porcentual:

```
* La primera nota vale un 15% del total
* La segunda nota vale un 35% del total
* La tercera nota vale un 50% del total

Ejemplos:
nota_1 = 10
nota_2 = 7
nota_3 = 4

```


## Consigna 5:  
### La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

🖐 Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista


Partirás de: 

```
matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

```

Debes llegar a: 

```
matriz = [ 
    [1, 5, 1, 7],
    [2, 1, 2, 5],
    [3, 0, 1, 4],
    [1, 4, 4, 9]
]

```


### >>Aspectos a incluir en el entregable:
Copia del documento con tus respuestas.

### Aspectos a tener en cuenta:
Los datos deben guardarse en variables y deben ser dinámicos por medio de input.


#### informacion adicional 
* https://www.freecodecamp.org/espanol/news/python-lista-append-como-agregar-elementos-a-una-lista-explicado-con-ejemplos/
* https://www.snakify.org/es/lessons/two_dimensional_lists_arrays/
* https://www.geeksforgeeks.org/