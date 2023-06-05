while True:
    valor = input("Ingresa un valor numérico: ")
    if valor.isdigit():  # Verifica si el valor ingresado es un número entero positivo
        valor = int(valor)
        break
    else:
        print("Valor no válido, sólo se pueden introducir valores numéricos.")

print("El valor ingresado es:", valor)