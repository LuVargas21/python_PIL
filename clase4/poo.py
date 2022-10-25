

# #EJERCICIO POO 
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.


from msilib.schema import Class


class Persona: 
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad 
        self.dni= dni

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self): 
        return self.__edad 
    
    @property
    def dni(self): 
        return self.__dni

    @dni.setter
    def validar_dni (self): 
     if len(self.__dni) == 8: 
        print ('Documento correcto')  
        self.__dni = " "
     else: 
        len(self.__dni) != 8  
        print ('Documento incorrecto')
        self.__dni = " "

    def dni(self, dni):
        self.__dni = dni 
        self.validar_dni()
    
    @edad.setter
    def validar_edad(self, edad):
        if edad >= 18: 
         print('Puedes acceder')
         self.__edad = " "
        else: 
         edad < 18 
         print('No puede acceder')
         self.__edad 

    def edad(self, edad): 
        self.__edad = edad 
        self.validar_edad()

    def mostrar(self):
        return "Nombre:"+self.nombre+" - Edad:"+str(self.edad)+" - DNI:"+self.dni


# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta: 
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad 
    
    @property
    def titular(self): 
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad 
    
    @titular.setter  
    def titular (self, titular):
        self.__titular = titular 
    
    def mostrar(self):
        return "Cuenta:\n" + "Titular:"+ self.titular.mostrar()+ "\n" + "Cantidad:"+ str(self.cantidad)

    # ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    def ingreso (self, cantidad): 
        if cantidad > 0: 
          self.__cantidad = self.cantidad + cantidad 
    
    def retiro (self, cantidad): 
        if cantidad > 0: 
            self.__cantidad = self.cantidad - cantidad 


# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:

# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
# Piensa los métodos heredados de la clase madre que hay que reescribir.


class CuentaJoven (Cuenta): 
