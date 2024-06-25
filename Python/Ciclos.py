#Ciclo While con este ciclo podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera.


#En este ciclo se realiza  con la variable condición un ciclo que se pone como limite 
# menor a 10 para que nos muestre un conteo desde el valor de condición hasta un valor antes del numero 10
condicion=0
while condicion < 10:
    print(condicion)
    condicion+=2

#En este ciclo se utiliza la sentencia break hasta llegar a 15 se detiene la ejecución
condicion1=0
while condicion1 < 20:
    condicion1 += 1
    if condicion1 == 15:
        print("Se detiene la ejecución")
        break
    print(condicion1)

# Ciclo for se usa para iterar sobre una secuencia

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#En estos ciclos for vemos el uso de la sentencia break y continue 
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}


for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")  



for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")