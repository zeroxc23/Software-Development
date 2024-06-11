#Ciclo While

condicion=0
while condicion < 10:
    print(condicion)
    condicion+=2


condicion1=0
while condicion1 < 20:
    condicion1 += 1
    if condicion1 == 15:
        print("Se detiene la ejecución")
        break
    print(condicion1)