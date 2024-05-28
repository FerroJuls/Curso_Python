
print("")
print("HALLAR LA AREA DEL TRIANGULO")

print("")
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es:", area)


print("")
print("SI UN NUMERO ES PRIMO O NO ")

numero = int(input("Ingrese un número entero positivo: "))
es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, (numero // 2) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("El número es primo.")
else:
    print("El número no es primo.")


