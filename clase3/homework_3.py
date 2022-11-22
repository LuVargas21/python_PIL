# FUNCIONES 

# def funcion_example (x, y):
#     resultado = x + y
#     return resultado

# # llamar a una funcion 

# resultado_suma = funcion_example (2, 3)
# print(resultado_suma)
# print (funcion_example (2, 3))

#Otras estructuras de  funciones. Sin parámetros 
#funcion2
# def resta (): 
#     resultado = 2-3 
#     return resultado

# print(resta())

#funcion3

# def saludo(nombre):
#     print('Hola', nombre)
# nombre = input('Ingrese su nombre')
# saludo('nombre')




# def saludo (cantidad_saludos): 
#    lista_nombre = [] #esta lista va a guardar los nombres que ingrese el usuario. Si esta afuera es global y permite que se la llame todo el codigo, en la variable local solo se puede usar en el bloque de codigo que se esta usando 
   
#    for i in range (cantidad_saludos):

#         nombre = input('Ingrese su nombre')
#         print ('Hola' + nombre)

#         lista_nombre.append(nombre)

#         return lista_nombre

# def orden(lista, sentido):
#     lista.sort (reverse=sentido) #sort ordena la lista
#     return lista

# nombres = saludo (int(input('Ingrese la cantidad de saludos')))

# print (orden (nombres, False))

#_____orden de los parametros
# def prueba (a,b,c):
#     print (c, a, b ) #si yo cambio el orden de los parámetros, los toma tal como los declaramos en la posición

# a= 420
# b=3
# c= 5
# prueba (a=a, b=b, c=c) #igualando los parametros siempre va a mostrar el valor, sin importar el orden en que yo pase los parámetros.
#__________

n = "1"
while True: 
    
        n1= int(input('Ingrese un número entero'))
        n2 = int(input('Ingrese un número entero'))

        if n1 >= 0  &  n1 < n2: 
            print('Los números pares dentro del rango ingresado son:')
 
            for n in range (n1, n2): 
                if n % 2 == 0: 
                 print (n)
        break
else: 
    print('Datos invalidos')

#}


#  CouponValidation function -> validates if the user has a discount coupon. It calculates and returns the total amount.   
  
#VALIDATION 
totalAmount=0
totalAmountDiscount = 0


def discountValidation (): 
  totalAmountDiscount = totalAmount * 0.05 
  return totalAmountDiscount 


def validationOption (): 
  print (input('Press "Y" for yes'))
  print (input('Press "N" for not')) 

coupon = True 
while coupon: 
  validationOption ()
  option = "" 
  option = input ('Do you have a discount coupon?')

  if option == "Y": 
   print(totalAmountDiscount)
   
  elif option == "N": 
    print('You do not have a discount this time :(')
    print (totalAmount) 
  break
