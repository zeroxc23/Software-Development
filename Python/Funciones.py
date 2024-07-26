# Funciones son bloques de codigo con un proceso en especifico que funcionan cuando son llamados

#Una función se define usan la palabra clave def

#Nota despues del def se agrega el nombre de la función y un () que indica el numero de parametros con el nombre que uno elija

def Funcion():
    print("Hola soy una función :v")

Funcion()

#Esta función por ejemplo determina entre 3 numeros cual es el mayor 

def maximo_tres(num1, num2, num3):
  
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3

mayor = maximo_tres(12, 8, 15)
print(f"El número máximo es: {mayor}")

#En esta función se utiliza el argumento *args que al añadir * 
#permite que la función reciba un numero indefinido de argumentos


def my_function(*kids):
  print("El niño mas joven es " + kids[2])

my_function("Emil", "Tobias", "Linus")

# En esta función se utiliza el argumento **kwargs que al añadir **
#recibira un diccionario de argumentos, y puede acceder a los elementos
def my_function(**kid):
  print("Su apellido es " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")