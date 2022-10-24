# class Gato: 
#     especie = 'mamifero'
#     def __init__(self, nombre, edad):
#         self.nombre= nombre
#         self.edad=edad
#         self.alimentos=[]
    
#     def verEtapaDeVida(self):
#         if self.edad>1:
#             print (self.nombre, 'Es adulto')
#         else:
#             print (self.nombre, 'Es cachorro')
    
#     def alimentoFavorito(self, alimento):
#         return alimento in self.alimentos


# p=Gato('Pelusa', 1)
# # p.verEtapaDeVida()

# p.edad= 3
# p.verEtapaDeVida()
# p.alimentos=["leche", "arroz"]
# print(p.alimentoFavorito("leche"))
# print(Gato.especie)


# #EJERCICIO POO 
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.


class Persona: 
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad 
        self.dni= dni

    def nombre(self):
        return self.__nombre
    
    def edad(self): 
        return self.__edad 
    
    def dni(self): 
        return self.__dni

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