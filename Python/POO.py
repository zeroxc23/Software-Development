#La Programación Orientada a Objetos (POO) en Python es un paradigma de programación que se basa en la creación 
# y manipulación de objetos, los cuales son instancias de clases.ç
#Ejemplo
class Miclase:     #Esta es la forma en la que la clase se define
    x=12           #Esto seria la propiedad de la clase

z=Miclase() #Desde aqui es cuando se creea el objeto
print(z.x) 
#Los ejemplos anteriores son clases y 
# objetos en su forma más simple, y 
# no son realmente útiles en aplicaciones de la vida real.

# Todas las clases tienen una función llamada __init__(), 
# que siempre se ejecuta cuando la clase se está iniciando.

#Se utiliza la función __init__() para asignar valores a las 
# propiedades del objeto u operaciones si es necesario.

class Persona:
    #Atributos de la clase Persona
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
       
 #Ahora a mostrar los datos de la persona
persona1=Persona("Luis",30,"Kr 15")
print(persona1.edad)

# La función __init__() se llama en las clases cada vez que se utiliza 
# la clase para crear un nuevo objeto.


#Ahora veremos la función __str__()
#La función __str__() se utiliza para mostrar los datos de un objeto.
class Persona1:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
    def __str__(self):
        return f"{self.nombre}({self.edad})"

persona1=Persona1("Luis",30,"Kr 15")
print(persona1) #Luis(30)

#Ahora con un metodo
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def myfunc(self):
    print("Hola mi nombre es » "+ self.nombre,self.edad)

p1 = Persona("Juan",36)
#Otras funciones 
#Modificar la propiedad de los objetos
p1.edad=40
print(p1.edad) #40
#Borrar la propiedad de los objetos
del p1.edad
print(p1.edad) #Error
#Borrar objetos
del p1
p1.myfunc()

#Sentencia pass
#La sentencia pass se utiliza para indicar que una función o un bloque de código no tiene
# ninguna acción que realizar. Por ejemplo, si se define una función pero no se
# especifica qué acciones realizar, se puede utilizar la sentencia pass para indicar
# que la función no tiene ninguna acción que realizar.
#Ejemplo de uso de la sentencia pass

class MiClase:
   pass




#Nota: El parámetro self es una referencia a la instancia actual de la clase, y
#se utiliza para acceder a variables que pertenecen a la clase.




      
         
