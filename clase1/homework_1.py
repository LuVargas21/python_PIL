# Idear la manera de realizar la siguiente salida (a, b y c son variables).:
#   a       b        c 
#  2.4    -3.21    47.8


#a= 'a'
#b= 'b'
#c= 'c'

#a1 = float(2.4)
#b1 = float(-3.21)
#c1 = float(47.8)

#print (a, '\t',b, '\t', c)
#print (a1,'\t', b1, '\t', c1)


#PROBLEMA 3
# Escriba un programa que lea 1 palabra (ingresadas por el usuario), calcule la longitud de cada una de ellas y las despliegue
#junto con su longitud indicada con asteriscos. Ejemplo:
# arbol *****
# hola ****

word = input('escriba una palabra')
wordreturn = '*'  * len(word) 
 
print (word + ' ' + wordreturn) 