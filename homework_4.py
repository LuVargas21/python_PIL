#PROGRAMACION ORIENTADA A OBJETOS. 

#DEFINIR LA CLASE 

class perro: 
  # atributos de clase // equivale a variable global . todos los objetos "perro" van a tener esas caracteristicas
  especie = 'mamiferos'

  def __init__(self, nombre, raza):  #constructor  #estamos indicando que queremos crear un objeto que se va a instanciar a si mismo. 
  #atributos  de instancia  // es el equivalente a variables locales porque son propios de cada objeto 
    self.nombre =  nombre
    self.raza = raza 

   #metodos  // funciones - acciones que hacen los objetos
  def ladrar (self):
        print ('guauguau')
    
  def jugar (self, objeto):  #se pueden pasar parametros
        print ('el perroe esta jugando con:' , objeto)   

  def saludar (self): 
        print ('guagu mi nombre es:', self.nombre)


perro1 = perro('rex', 'collie')
    #imprime las características-
#print(perro1.raza)  
#print(perro1.nombre)

print (f'perro1 -> {perro1.nombre}, {perro1.raza} , {perro1.especie} ')
perro1.ladrar()
perro1.jugar('pelota')
perro1.saludar()

#creamos otro objeto 
perro2 = perro('ana', 'collie')
print (f'perro2 -> {perro2.nombre}, {perro2.raza} ')

perro2.saludar()