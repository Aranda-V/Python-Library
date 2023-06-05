#FASE 1 DE LA PRUEBA
print("Paso 1: \n")

nombre = "viCtOr aRanDa"

print("Original: ",nombre)

#Aplicamos la corrección con .title()
print("Corregido: ",nombre.title())

#Confirmamos que al estar MAL escrito, el resultado de istitle() es "False"
if nombre.istitle() == False :
    print("\nEstá mal escrito")
else :
    print("Algo raro pasa")

#FASE 2 DE LA PRUEBA
print("\nPaso 2: \n")

nombre2 = "Victor Aranda"

print(nombre2)

#Confirmamos que al estar BIEN escrito, el resultado de istitle() es "True"
if nombre2.istitle() == True :
    print("\nEstá bien escrito")