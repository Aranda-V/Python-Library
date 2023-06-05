#TÍTULO PARA HACER BONITO

print("\n||==============================||")
print("|| CONSULTAS VACACIONALES RAPPI ||")
print("||==============================|| \n")

#PRIMERO PEDIR LOS DATOS E INTRODUCIRLOS EN LAS VARIABLES

nombre = input("Introduce tu nombre: ")

#MOSTRAR LOS DIFERENTES DEPARTAMENTOS

print("\n||===============||")
print("|| Departamentos ||")
print("||===============|| \n")

print("1 - Atención al cliente")
print("2 - Logística")
print("3 - Gerencia \n")

#PEDIR A QUÉ DEPARTAMENTO PERTENECE EL USUARIO

departamento = input("Introduce el número de tu departamento: ")

departamento = int(departamento)

#PEDIR CUÁNTOS AÑOS COMPLETOS LLEVA TRABAJANDO EN LA EMPRESA

anos = input("\nIntroduce el número de años COMPLETOS que llevas en la empresa: ")

anos = int(anos)

#A PARTIR DE AQUÍ IF PARA LLEVAR SEGÚN DEPARTAMENTO

if departamento == 1 :
   
    if anos < 1 :
        print("\nLo sentimos, ", nombre, ", todavía no tienes derecho a días de vacaciones\n")

    elif anos == 1 :
        print("\n",nombre,", tienes derecho a 6 días de vacaciones.\n")

    elif anos >= 2 and anos <= 6 :
        print("\n",nombre,", tienes derecho a 14 días de vacaciones.\n")

    elif anos >= 7 :
        print("\n",nombre,", tienes derecho a 20 días de vacaciones.\n")
    
    else :
        print("\nNo se reconoce el número de años trabajados.\n")

if departamento == 2 :
   
    if anos < 1 :
        print("\nLo sentimos, ", nombre, ", todavía no tienes derecho a días de vacaciones\n")

    elif anos == 1 :
        print("\n",nombre,", tienes derecho a 7 días de vacaciones.\n")

    elif anos >= 2 and anos <= 6 :
        print("\n",nombre,", tienes derecho a 15 días de vacaciones.\n")

    elif anos >= 7 :
        print("\n",nombre,", tienes derecho a 22 días de vacaciones.\n")
    
    else :
        print("No se reconoce el número de años trabajados.\n")

if departamento == 3 :
   
    if anos < 1 :
        print("\nLo sentimos, ", nombre, ", todavía no tienes derecho a días de vacaciones\n")

    elif anos == 1 :
        print("\n",nombre,", tienes derecho a 10 días de vacaciones.\n")

    elif anos >= 2 and anos <= 6 :
        print("\n",nombre,", tienes derecho a 20 días de vacaciones.\n")

    elif anos >= 7 :
        print("\n",nombre,", tienes derecho a 30 días de vacaciones.\n")
    
    else :
        print("No se reconoce el número de años trabajados.\n")

print("Que tengas un buen día en Rappi S.A.")