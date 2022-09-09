
# EJERCICIO1
# REALIZAR UN MENU DE CAJERO AUTOMATICO DONDE EL USUARIO PUEDA ESCOGER ENTRE ALGUNA
# DE LAS SIGUIENTES OPCIONES
# * DEPOSITO
# * EXTRACCIÓN
# * TRANSFRENCIA
# * SALIR

# EN TODOS LOS CASOS SE LE PEDIRA AL USUARIO INGRESAR UN MONTO DE DINERO Y EL PROGRAMA DEBERA MOSTRAR EN TODO MOMENTO
# LA SECCIÓN DEL MENU EN LA QUE SE ENCUENTRE, PUDIENDO RETORNAR AL MENU PRINCIPAL SIEMPRE QUE SE QUIERA
# Y SOLO SE DETENDRÁ LA EJECUCUÓN CUANDO INGRESE LA OPCION SALIR EN EL MENU PRINCIPAL

print('Bienvenido a e-Bank')


def processOperation(operation):
    if (operation != ""):
     goBack = True
     while goBack:
       option_exit = input('Ingrese el monto a' + ' ' + operation +'\n O presione "0" para volver al menú principal')
       if (option_exit == "0"):
        print ('Volver al menu principal')
    else: 
        print ('Volver al menu anterior')
    

def mainMenu():
  print('1.Depositos')
  print('2.Extracciones')
  print('3.Transferencia')
  print('4.Salir')


atm = True
while atm:
    mainMenu()
    operation = ""
    option = int(input('Ingrese la operación que desea realizar'))

    if int(option) == 1:
     processOperation('Depositar')

    elif int(option) == 2:
     processOperation('Extraer')

    elif int(option)== 3:
     processOperation('Transferir')

    elif int(option) == 4: 
        processOperation('Salir')
        print('volver a la pantalla principal')
        atm = False 
        break
else: 
     print('Seleccione una opción válida')


# EJERCICIO2
#idear un programa que solicite al usuario dos números enteros y el programa
#deberá retornar aquellos números pares que se encuentren dentro del rango
# formado entre los números ingresados.

n = "1"
while True: 
    
        n1= int(input('Ingrese un número entero'))
        n2 = int(input('Ingrese un número entero'))

        if n1 >= 0  &  n1 < n2: 
            print('Los números pares dentro del rango ingresado son:')

else: 
    print('Datos invalidos')

    