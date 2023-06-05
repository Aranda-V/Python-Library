#Aquí pide el nombre al usuario:

nombre = input("Introduce tu nombre: ")

print("Hola ", nombre, ", vamos a ver si pasas de curso:")



#Ahora aquí pide los resultados de las notas:

nota1 = float(input("Introduce tu nota de matemáticas: "))
nota2 = float(input("Introduce tu nota de química: "))
nota3 = float(input("Introduce tu nota de geografía: "))
nota4 = float(input("Introduce tu nota de historia: "))



#Ahora aquí realiza la media de la nota:

total = nota1 + nota2 + nota3 + nota4

media = total/4

#También se puede hacer como "media = (nota1 + nota2 + nota3 + nota4) / 4"



#Ahora compara la nota media con el mínimo para superar el curso y decide que función realiza:
#Con el comando "round" redondeamos a 2 decimales:

if media>=7:
    print("Tu nota media es:", round(media,2), ", por tanto pasas de curso. ¡Felicidades!")
    
else:
    print("Tu nota media es:", round(media,2), ", por tanto no pasas de curso.")

print("Adiós")
