print(" ")
print("===============")
print("| PAR O IMPAR |")
print("===============")
print(" ")
num = input("Introduce un número entero: ")

num = int(num)

print(" ")

residuo = (num % 2)

if residuo > 0 :
    print("El número", num, "es impar")

else :
    print("El número", num, "es par")

print(" ")
print("FIN")