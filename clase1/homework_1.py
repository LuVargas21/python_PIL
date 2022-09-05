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

#PROBLEMA 2 
import pyfiglet
titulo = pyfiglet.figlet_format("hola mundo <3")
print(titulo)

#PROBLEMA 3
# Escriba un programa que lea 1 palabra (ingresadas por el usuario), calcule la longitud de cada una de ellas y las despliegue
#junto con su longitud indicada con asteriscos. Ejemplo:
# arbol *****
# hola ****

#word = input("write your name")
#wordreturn = '*'  * len(word) 
 
# print (word + ' ' + wordreturn) 


#PROBLEMA 4
# Crear un diccionario del ejercicio anterior 

#dictionary = {
    #"name" : "Luciana", 
    #"age" : 28, 
    #"identification" : 37438775, 
    #"passport" : True
#}

#print (dictorinary["nombre"])  accedo al value de esa key
# print(dictionary (d1.get('nombre)) es otro metodo para acceder al  value

#agrega un key value que no existia  

#dictionary["address"] = "24 de septiembre 974"

# imprimir los key 
#for x in dictionary: 
    #print(x)

# imprimir los value de las key
 #for x in dictionary:
     #print (dictionary [x])

#imprimir ambos valores a la vez.  x e y 

#for x, y in dictionary.items():
    #print(x,y)

#diccionarios anidados

#dic1 = {"name" : "Luciana", 
 #  "age" : 28, 
#   "identification" : 37438775, 
#   "passport" : True
#    } 
#dic2 = {"name" : "Julia", 
 #   "age" : 24, 
  #  "identification" : 40504496, 
   # "passport" : False,
    #"address" : "Moreno 100"
#}

#d = { 
 #   "dic1" : dic1, 
#   "dic2" : dic2
# }

#permite obtner el value para una key
#print(dic2.get("name")) 

#ITEMS
#items el metodo item() devuelve una lista con los key y las values  
#si se convierte en list se puede indexar como una lista
# los primeros elementos son key y el segundo value 

#it = dic1.items()
# print (it) #dic1_items ([("a", 1)....])
# print (list(it))  #[("a", 1)] lo imprime como una lista

#print(list(it)[1]) # ("a", 1) devuelve el  key y el contenido de ese item especifico  

#KEYS()

#devuelve una lista con todas las key del diccionario 

#k = dic2.keys()
#print (k)   #dic2_keys (["a", "b".....])
#print(list(k)) # los imprime como una lista

#VALUES()

#devuelve una lista con todos los values del diccionario

#print(list(dic1.values()))

#POP()

#permite eliminar una key que se pasa como parametro 

#dic2.pop("age")  #elimine la key "age" y su value
#print (dic2) 

#POPITEM() elimina de manera aleatoria un elemento del diccionario
 
 #dic1.popitem()
#print(dic1) 


#UPDATE(<OBJ>)
#se llama sobre un diccionario y tiene como entrada otro diccionario. 
#los value son actualizados y si no esta algun value del nuevo dicc se añade 

#dic1.update(dic2)
#print(dic1)  en el diccionario 1 no esta presente la key "address"
#el print muestra la key address que  si está en el  el dic2. 
