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

    print("======== MENÚ ========")
    print("1. Añadir asignatura")
    print("2. Ver Asignaturas")
    print("3. Ingrese su nota")
    print("4. Salir del programa")

    opcion = int(input("\nIngrese una opción: "))
    print("\n" * 4)

    if opcion == 1:
        materia = str(input("Ingresa tu asignatura: "))
        Asginaturas.append(materia)
        print("\n" * 4)

    # Aqui no puedo ingresar sin tener datos en Scores | Me gustaria poder ver las materias antes de ingresar las notas
    if opcion == 2:
        for i in range(len(Asginaturas)):
            print("En " + Asginaturas[i] + " has sacado " + Scores[i])
        print("\n" * 4)

    if opcion == 3:
        for materia in Asginaturas:
            score = input(f"¿Que nota sacaste en {materia}? ")
            Scores.append(score)
        print("\n")

    if opcion == 4:
        print("\n" * 50)
        print("Has salido del programa")
        print("\n" * 4)
        break