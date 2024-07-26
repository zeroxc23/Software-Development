# Las condicionales son una sección código que ejecuta si se cumplen las condiciones
# Utilizando las sentencias if, elif y else


#Sentencia if
a = 78
b = 570
if b > a:
    print("B es mayor que A")

#Sentencia elif
condicion= 6 * 6

if condicion > 10 and condicion < 30:
    print("El resultado esta entre el rango de 10 y 30")
elif condicion > 30 and condicion < 50:
     print("El resultado esta entre el rango de 30 y 50")
     
#Sentencia else
a= 300
b=100

if b> a:
    print("B es mayor que A")

elif a == b:
    print("A es igual que B")
else:
    print("A es mayor que B")