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