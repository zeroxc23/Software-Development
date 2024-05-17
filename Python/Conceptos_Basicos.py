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
'''''Nombre=input("Ingresa tu nombre:")
Edad=input("Ingrese su edad:")
print("Tu nombre es:",Nombre)
print("Tu edad es:",Edad)
'''''
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

