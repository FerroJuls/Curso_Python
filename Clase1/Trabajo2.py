print("") 
print("") 

numero = 10

if numero > 0:
    print("El número",numero,"es positivo")
else:
    print("El número",numero,"es negativo o cero")
    
print("") 
print("") 

numero = -10

if numero > 0:
    print("El número",numero,"es positivo")
else:
    print("El número",numero,"es negativo o cero")

print("") 
print("") 

numero = 0

if numero > 0:
    print("El número",numero,"es positivo")
elif numero < 0:
    print("El número",numero,"es negativo")
else:
    print("El número",numero,"es neutro")


print("") 
print("") 

# La estructura de control while se utiliza para repetir un bloque de
# código mientras una condición sea verdadera.

contador = 0
while contador <= 10:
    print(contador)
    contador += 2

# La estructura de control for se utiliza para iterar sobre una secuencia de
# elementos, como una lista o una cadena de caracteres

frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# La estructura de control for también se puede utilizar con la función
# range() para generar una secuencia de números en un rango específico
# En este caso, el for itera sobre los números del 1 al 5 y los imprime en
# cada iteración.

for i in range(1, 6):
    print(i)







