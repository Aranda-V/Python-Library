print(" ")
print("=================")
print("| EL MÁS GRANDE |")
print("=================")
print(" ")

num1 = input("Introduce el primer número: ")
num1 = int(num1)

print(" ")

num2 = input("Introduce el segundo número: ")
num2 = int(num2)

print(" ")

num3 = input("Introduce el tercero número: ")
num3 = int(num3)

print(" ")

if num1 > num2 and num1 > num3 :
    print("El número", num1,"es el más grande de los tres")

elif num2 > num1 and num2 > num3 :
    print("El número", num2,"es el más grande de los tres")

else :
    print("El número", num3,"es el más grande de los tres")

print(" ")

print("FIN")