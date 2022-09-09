#EJERCICIO 3
# Idear la manera de realizar la siguiente salida (a, b y c son variables).:
#   a       b        c 
#  2.4    -3.21    47.8

a= 'a'
b= 'b'
c= 'c'

a1 = float(2.4)
b1 = float(-3.21)
c1 = float(47.8)

print (a, '\t',b, '\t', c)
print (a1,'\t', b1, '\t', c1)

 
#PROBLEMA 3
# Escriba un programa que lea 1 palabra (ingresadas por el usuario), calcule la longitud de cada una de ellas y las despliegue
#junto con su longitud indicada con asteriscos. Ejemplo:
# arbol *****
# hola ****

word = input("write your name")
wordreturn = '*'  * len(word) 
 
print (word + ' ' + wordreturn) 


#PROBLEMA 4
# Crear un diccionario 

dictionary = {
    "name" : "Luciana", 
    "age" : 28, 
    "identification" : 37438775, 
    "passport" : True
}

print (dictionary ["nombre"]) 
print(dictionary.get('nombre'))

#agrega un key value que no existia  

dictionary["address"] = "24 de septiembre 974"

# imprimir los key 
for x in dictionary: 
    print(x)

# imprimir los value de las key
for x in dictionary:
     print (dictionary [x])

#imprimir ambos valores a la vez.  x e y 

for x, y in dictionary.items():
    print(x,y)

#diccionarios anidados

dic1 = {"name" : "Luciana", 
   "age" : 28, 
  "identification" : 37438775, 
  "passport" : True
   } 
dic2 = {"name" : "Julia", 
   "age" : 24, 
   "identification" : 40504496, 
   "passport" : False,
   "address" : "Moreno 100"
}
print(dic1 + dic2)
