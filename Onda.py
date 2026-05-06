from random import randint

limite_minimo = int(input("Ingrese el rango minimo: "))
limite_maximo = int(input("Ingrese el rango maximo: "))

frecuencia_obejetivo = randint(limite_minimo, limite_maximo)

if frecuencia_obejetivo % 5 == 0:
    if frecuencia_obejetivo + 1 <= limite_maximo:
        frecuencia_obejetivo += 1
    else:
        frecuencia_obejetivo -= 1

adivinado = False

#Pimero intento

intento1 = int(input("Intento 1 - Ingrese la frecuecnia a calibrar: "))
if intento1 == frecuencia_obejetivo:
    print("Calibracion exitosa")
    adivinado = True
else:
    if frecuencia_obejetivo > intento1:
        print("La frecuencia a calibrar es mayor")
    else:
        print("La frecuencia a calibrar es menor")


#Segundo intento

if not adivinado:
    intento2 = int(input("Intento 2 - Ingrese la frecuencia a calibrar: "))
    if intento2 == frecuencia_obejetivo:
        print("Calibracion exitosa")
        adivinado = True
    else:
        if frecuencia_obejetivo > intento2:
            print("La frecuencia a calibrar es mayor")
        else:
            print("La frecuencia a calibrar es menor")

# Pista matematica utilizando valor absoluto

distancia1= abs(frecuencia_obejetivo - intento1)
distancia2= abs(frecuencia_obejetivo - intento2)    

print("Te daré una pista")
if distancia1 < distancia2:
    print(f"La frecuencia a calibrar esta mas cerca de {intento1} que de {intento2}")
elif distancia2 < distancia1:
    print(f"La frecuencia a calibrar esta mas cerca de {intento2} que de {intento1}")
else:
    print("Ambos intentos estuvieron a la misma distanciai numérica")

#Tercer intento

if not adivinado:
    intento3 = int(input("Intento 3 - Ingrese la ultima frecuecnia a calibrar: "))
    if intento3 == frecuencia_obejetivo:
        print("Calibracion exitosa")
        adivinado = True
    else:
        print("Calibracion fallida, la frecuencia correcta era: ", frecuencia_obejetivo)
