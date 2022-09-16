#PROGRAMACION ORIENTADA A OBJETOS. 

#CLASE PADRE 
class animal: 
 def __init__(self, especie, edad ): 
    self.especie = especie 
    self.edad = edad 

#metodos 
 def ruidoDeAnimal (self, sonido): 
    print (sonido) 
    


#DEFINIR CLASE HIJO 
class perro (animal) :  # aca estamos  haciendo que perro herede "animal" a traves de los () 
  # atributos de clase // equivale a variable global . todos los objetos "perro" van a tener esas caracteristicas
  #especie = 'canino'   # en este caso no lo necesitamos declarar porque ya lo va a heredar de animal..

  def __init__(self, nombre, raza, especie, edad):  #constructor  #estamos indicando que queremos crear un objeto que se va a instanciar a si mismo. 
  #atributos  de instancia  // es el equivalente a variables locales porque son propios de cada objeto 
    self.nombre =  nombre
    self.raza = raza 
    super(). __init__(especie, edad) 
   
   #metodos  // funciones - acciones que hacen los objetos
  
 
 # def jugar (self, objeto):  #se pueden pasar parametros
  #      print ('el perroe esta jugando con:' , objeto)   

  def saludar (self): 
        print (f'{self.nombre} dio la pata')
 

 #_____________INTANCIO OTRO OBJETO  QUE HEREDARÁ LA CLASE ANIMALES ________
class gato (animal):
    def __init__(self, nombre, raza, especie, edad):
        self.nombre= nombre
        self.raza = raza
        super().__init__(especie, edad)

#metodo 

def saludar (self): 
        print (f'{self.nombre} ronronea')
 


#IINSTANCIAR OBJETOS 
# Esta es una forma de hacerlo 
#perro1 = perro('rex', 'collie')
    #imprime las características-
#print(perro1.raza)  
#print(perro1.nombre)

#print (f'perro1 -> {perro1.nombre}, {perro1.raza} , {perro1.especie} ')
#perro1.ladrar()
#perro1.jugar('pelota')
#perro1.saludar()


# Y esta es otra forma, asignando directamente el nombre y la raza aca.
 #perro1 = perro ()
 #perro1.nombre = "Fermina"
 #perro1.nombre = "salchicha"


#creamos otro objeto 
#perro2 = perro('ana', 'collie')
#print (f'perro2 -> {perro2.nombre}, {perro2.raza} ')

#perro2.saludar()

#PARA OBJETOS CON HERENCIA 

#INSTANCIAR UN OBJETO 
perro1 = perro('firu', 'salchicha', 'perro', 5)
print(f'perro1 -> {perro1.nombre}, {perro1.raza}, {perro1.especie}, {perro1.edad} ')
perro1.saludar () 
 
 
gato1 = gato('Jenni', 'siames', 'gato', 2)
print(f'gato1 -> {gato1.nombre}, {gato1.raza}, {gato1.especie}, {gato1.edad}')