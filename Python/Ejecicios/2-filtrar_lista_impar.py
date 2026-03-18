# Ejercicio 2 - Filtrar Índices Impares de Lista
#
# Realiza un algoritmo que imprima solo los elementos
# correspondientes a un índice impar de la siguiente lista:
# arr = [1, "Pepe", 132, "Está", "Cometiendo", "estudiando",
#        "crímenes", "programación", "de", "ahora"]

arr = [1, "Pepe", 132, "Está", "Cometiendo", "estudiando",
       "crímenes", "programación", "de", "ahora"]

for i in range(len(arr)):
    if i % 2 != 0:
        print(f"Índice {i}: {arr[i]}")