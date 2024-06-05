# 1. Definir una función max() que tome como argumento dos números y devuelva el
# mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero
# hacerla nosotros mismos es un muy buen ejercicio.
# print()
# print("EJERCICIO 1" )
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))

# def max(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# print(max(num1, num2)) 
# print() 





# 2. Definir una función max_de_tres(), que tome tres números como argumentos y
# devuelva el mayor de ellos.
# print()
# print("EJERCICIO 2" )
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
# num3 = int(input("Ingrese el tercer número: "))

# def max(num1, num2, num3):
#     if num1 > num2:
#         return num1
#     elif num2 > num3:
#         return num2
#     else:
#         return num3

# print(max(num1, num2, num3)) 
# print()





# 3. Cuando se envían mensajes de texto o se tuitea, no es raro abreviar las palabras
# para ahorrar tiempo o espacio, como por ejemplo omitiendo las vocales, tal y como
# Twitter fue originalmente llamado "twttr". En un archivo llamado twttr.py, implementa
# un programa que solicite al usuario una cadena de texto y luego muestre esa misma
# cadena de texto, pero sin todas las vocales (A, E, I, O y U), ya sea que hayan sido
# ingresadas en mayúsculas o minúsculas.

        # CODIGO ERRONEO 
        # def main():
        #     palabra = input("Ingrese una palabra: ")
        #     resultado = twttr (palabra)
        #     print ("La palabra abrevida es: " + "join(resultado)")

        # twttr(pal):
        #     pal.lower()
        #     sal=[]
        #     for z in range(len(pal):
        #     pal[z] not in ["a","e","i","o","u" "]:
        #     sal.append(pal[z])
        #     return sal

        #     if __name__ =="__main__":
        #     main();



# print()
# print("EJERCICIO 3" )
# def main():
#     palabra = input("Ingrese una palabra: ")
#     resultado = twttr(palabra)
#     print("La palabra abreviada es: " + ''.join(resultado))

# def twttr(pal):
#     pal = pal.lower()
#     sal = []
#     for z in range(len(pal)):
#         if pal[z] not in ["a", "e", "i", "o", "u"]:
#             sal.append(pal[z])
#     return sal

# if __name__ == "__main__":
#     main()


# Los errore que tenia el codigo anterior son:
# 1. No se declaro la funcion / twttr(pal): = def twttr(pal):
# 2. Variable pal en / pal.lower() = pal = pal.lower()
# 3. En el sigiente apartado se habian comillad de mas / pal[z] not in ["a","e","i","o","u" "]: = if pal[z] not in ["a", "e", "i", "o", "u"]:
# 4. El join estaba con comillas / print ("La palabra abrevida es: " + "join(resultado)") = print("La palabra abreviada es: " + ''.join(resultado))
# 5. El main tenia / main(); = main()





# 4. Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
# contrario devuelve False.
   

# print()
# print("EJERCICIO 4" )
# letra = input("Ingrese una letra: ")

# def vocal(letra):
#     if letra in ['A', 'E', 'I', 'O', 'U','a', 'e', 'i', 'o', 'u', ]:
#         return True
#     else:
#         return False

# print(vocal(letra)) 





# 5. Escribir una función sum() y una función multip() que sumen y multipliquen
# respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
# devolver 10 y multip([1,2,3,4]) debería devolver 24.


print()
print("EJERCICIO 5" )
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def multip(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

print(sum([1, 2, 3, 4]))  
print(multip([1, 2, 3, 4]))  