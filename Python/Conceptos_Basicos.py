#Hola mundo muestra de como responde el lenguaje maquina
print('Hola Mundo')

#Comentario de una linea

"""
Comentario
de
varias
lineas
"""
'''Igual 
pero 
con 
comillas 
simples'''

#Type= sirve para saber el tipo de dato
print(type("Soy un dato str"))  # Tipo 'str'
print(type(5))  # Tipo 'int'
print(type(1.5))  # Tipo 'float'
print(type(3 + 1j))  # Tipo 'complex'
print(type(True))  # Tipo 'bool'
print(type(print("Mi cadena de texto")))  # Tipo 'NoneType'

'Variables'

Var= 'Mi variable de tipo texto'
print(Var)

'Variable tipo númerico (int)'
Var1= 5
print(Var1)

'Variable tipo booleano'
Var2=False
print(Var2)


'Variables en una sola linea'
a, b, c, d= "Hola", 3, 'Objeto',1
print('Saludo',a,'Numero',b,'Palabra',c,'Numero',d)

'Se puede forzar el tipo de dato a la variable'
Num:int=2
print(Num)

'Variable tipo Input'
Nombre=input("Ingresa tu nombre:")
Edad=input("Ingrese su edad:")
print("Tu nombre es:",Nombre)
print("Tu edad es:",Edad)

'Operadores'

'Operaciones con numeros enteros'
print(3+4) # '+' Suma
print(3-4) # '-' Resta
print(3*4) # '*' Multiplicación
print(3/4) # '/' División
print(10 % 3) # '%' Devuelve el residuo de la división
print(10 // 3) # '//' División entera
print(2 ** 3) # '**' Potenciación

'Tambien funciona con cadenas de texto'
print("Hola " + "Python " + "¿Qué tal?")

'Operadores comparativos'
print(3 > 4) # False
print(3 < 4) # True
print(3 >= 4) # False
print(4 <= 4) # True
print(3 == 4) # False
print(3 != 4) # True

# Con cadenas de texto
print("Hola" > "Python") # False
print("Hola" < "Python") # True

'Operadores logicos'
print(1<5 or 8<1) # or si alguno es correcto
print(3 > 4 and "Hola" > "Python") # and si los dos son correctos
print(not (3 > 4)) #not Forzar si es correcto o no

'Strings'
Mi_string='Mi otro string'

'Len Funciona para contar los caracteres incluyendo el espacio= ' ' '
print(len('Hola'))
'----------------------------------------------------'
'Modo de usar los strings'
print('Hola\n como\n estan')# \n significa salto de linea
print(' \tHola mundo ')# \t significa tabulación
print('\\t Hola Mundo \\n._.') #Escapado


'Formateo'

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

'División'
Divi= 'LENGUAJE'
print(Divi[1:3])
print(Divi[1:])
print(Divi[-2])
print(Divi[0:6:2])

'Funciones del lenguaje'
# Convierte la primera letra de la cadena en mayúscula y el resto en minúscula.
print(Divi.capitalize())

# Convierte todas las letras de la cadena en mayúsculas.
print(Divi.upper())

# Cuenta cuántas veces aparece la letra 'N' en la cadena.
print(Divi.count("N"))

# Verifica si la cadena está compuesta solo por números.
print(Divi.isnumeric())

# Verifica si la cadena '1' está compuesta solo por números.
print("1".isnumeric())

# Convierte todas las letras de la cadena en minúsculas.
print(Divi.lower())

# Convierte todas las letras de la cadena en minúsculas y luego verifica si la cadena resultante está en mayúsculas (siempre será False).
print(Divi.lower().isupper())

# Verifica si la cadena comienza con la subcadena "LEN".
print(Divi.startswith("LEN"))


'----------------------------------------------------'
#Listas se utilizan para almacenar múltiples elementos en una sola variable.
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)

#Tuplas se utilizan para almacenar múltiples elementos en una sola variable.

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
print(my_tuple)


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Sets se utilizan para almacenar múltiples elementos en una sola variable.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Diccionarios se utilizan para almacenar valores de datos en pares clave:value.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_dict)