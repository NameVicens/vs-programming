#Para este ejercicio se pedirá un diseño simple que compare la
#multiplicación de variables ingresadas por el usuario. Lo primordial es que
#el programa indique si el resultado de la multiplicación es par o impar.

#Se solicita los dos numeros al usario, y luego se multiplicara
var1 = int(input("Ingrese el primer número: "))
var2 = int(input("Ingrese el segundo número: "))


#Aqui se va a multiplicar 
resultado = var1 * var2

ver = resultado%2

if ver == 0:
    print(f"El resultado de {var1} x {var2} = {resultado} por ello es par")

else:
    print(f"El resultado de {var1} x {var2} = {resultado} por ello es inpar")