print("=========")
print("Conversor")
print("========= \n")

print("Menú de opciones: \n")

print("Escribe 1 para convertir de números a letras")
print("Escribe 2 para convertir de letras a números \n")

opcion = int(input("Escribe tu selección: "))

if opcion == 1:
    print("\n Conversor de números a letras \n")

    var1 = int(input("Introduce un número entre el 1 y el 4: "))

    if var1 == 1:
        print("\n El número es 'UNO' \n")

    elif var1 == 2:
        print("\n El número es 'DOS' \n")

    elif var1 == 3:
        print("\n El número es 'TRES' \n")

    elif var1 == 4:
        print("\n El número es 'CUATRO' \n")

    else:
        print("\n Número no disponible \n")

elif opcion == 2:
    print("\n Conversor de letras a números \n")

    var1 = input("Introduce un número entre el uno y el cuatro: ")
    var1 = var1.lower()

    if var1 == "uno":
        print("\n El número es '1' \n")

    elif var1 == "dos":
        print("\n El número es '2' \n")

    elif var1 == "tres":
        print("\n El número es '3' \n")

    elif var1 == "cuatro":
        print("\n El número es '4' \n")

    else:
        print("\n Número no disponible \n")

else:
    print("\n Opción no disponible \n")

print("FIN")
