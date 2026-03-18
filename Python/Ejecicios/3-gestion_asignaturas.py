# Ejercicio 3 - Gestión de Asignaturas
#
# Escribe un programa que almacene las asignaturas de un curso
# (Matemáticas, Física, Química, Historia y Lengua) en una lista.
# El programa debe:
# 1. Mostrar la lista de asignaturas por pantalla.
# 2. Mostrar el mensaje "Yo estudio <asignatura>" para cada una.
# 3. Preguntar al usuario la nota obtenida en cada asignatura
#    y mostrar "En <asignatura> has sacado <nota>".

Asginaturas = []
Scores = []


while True:

    print("\n======== MENÚ ========")
    print("1. Añadir asignatura")
    print("2. Ver Asginaturas")
    print("3. Ingrese su nota")
    print("4. Salir del programa")
    print("\n")
    
    opcion = int(input("Ingrese una opción: "))
    print("\n" * 4)
    
    if opcion == 1:
        
        materia = str(input("Ingresa tu asignatura: "))
        Asginaturas.append(materia)
        print("\n" * 4)

    if opcion == 2:
        for i in range(len(Asginaturas)):
            print("Has tenido", Asginaturas[i])
            print("\n" * 4)

    if opcion == 3:
        print("Proximamente")
        print("\n" * 4)

    if opcion == 4:
        
        print("\n" * 50)
        print("Has salido del programa")
        print("\n" * 4)
        break
