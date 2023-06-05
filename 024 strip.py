#Utilizando el comando .strip() elimina los dos espacios de los extremos:

cadena1 = " Hola Víctor "

cadena1 = cadena1.strip()

print(cadena1)


#Aquí le indicamos qué caracteres ha de borrar, y lo hará en orden y en bucle hasta que ya no tenga nada que eliminar

cadena2 = " Hola Víctor "

cadena2 = cadena2.strip("o rHV")

#Primero prueba con una "o" en los extremos, pasa al espacio, pasa a la "r"... y cuando termina con la V vuelve a comenzar hasta que ya no tiene coincidencias

print(cadena2)

#De igual manera funcionaría con lstrip y rstrip