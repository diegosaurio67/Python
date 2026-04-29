while True:
    print("Menú")
    print("1.- Ver tabla de multiplicar")
    print("2.-salir")

    opcion = input("Seleccione una opcion (1-2): ")


    if opcion == "1":
        num = int(input("¿De que numero quiere la tabla?"))
        cont = 1
        while cont <= 10:
            print(f"{num} * {cont} = {num * cont}")   
            cont += 1
    elif opcion == "2":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida, intente de nuevo.")