print('Bienvenido a e-Bank')

def processOperation(operacion):
 if(operacion != ""):
    isBack = True 
    while isBack:
        option_exit = input('Ingrese el monto a ' + operacion + ' o  presione "Z" para volver al menú anterior:')
        if option_exit == "Z": 
            break
        
def print_menu():
 print('1: Depósito')
 print('2: Extracción')
 print('3: Tranaferencia')
 print('4: Salir')

goOn = True
while goOn:
  print_menu()
  operacion = ""
  option = input('Ingrese el número de operación que desea realizar:')
  if int(option) == 1:
    processOperation("depositar")
  elif int(option) == 2:
    processOperation("extraer")
  elif int(option) == 3:
    processOperation("transferir")
  elif int(option) == 4:
    print('volver a la pantalla principal')
    goOn = False
    break
  else:
    print('Opción inválida')