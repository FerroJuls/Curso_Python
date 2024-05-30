# var = 55
# print(var == 0)

# var = 99
# print(var == 0)

# var = 100
# print(var == 100)

# var = 101
# print(var == 101)

# var = -5
# print(var == 5)

# var = 123
# print(var == 123)

# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
 
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
 
# print("El número más grande es:", larger_number)


# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))
 

# largest_number = number1
 
# if number2 > largest_number:
#     largest_number = number2
 
# if number3 > largest_number:
#     largest_number = number3
 
# print("El número más grande es:", largest_number)


 
# number1 = int(input("Ingresa el primer número: "))
# number2 = int(input("Ingresa el segundo número: "))
# number3 = int(input("Ingresa el tercer número: "))
 

 
# largest_number = max(number1, number2, number3)
 
# print("El número más grande es:", largest_number)

 
# tex1 = str(input("Escribe la palabra secreta:"))
 
# if tex1 == "espatifilo":
#     print("No, ¡quiero un gran Espatifilo!")
# elif tex1 == "pelargonio":
#     print("¡Espatifilo!, ¡No pelargonio!")
# else:
#     print("Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!")


# income = float(input("Introduce el ingreso anual: "))

# if income < 85528:
# 	tax = income * 0.18 - 556.02
# else:
# 	tax = (income - 85528) * 0.32 + 14839.02

# if tax < 0.0:
# 	tax = 0.0

# tax = round(tax, 0)
# print("El impuesto es:", tax, "pesos")
 
# year = int(input("Introduce un año: "))

# if year < 1582:
#     print("No esta dentro del período del calendario Gregoriano")
# else:
#     if year % 4 != 0:
#         print("Año Común")
#     elif year % 100 != 0:
#         print("Año Bisiesto")
#     elif year % 400 != 0:
#         print("Año Común")
#     else:
#         print("Año Bisiesto")


# x, y, z = 5, 10, 8
 
# print(x > z)
# print((y - 5) == x)

# x = 10
 
# if x == 10:
#     print(x == 10)
# if x > 5:
#     print(x > 5)
# if x < 10:
#     print(x < 10)
# else:
#     print("else")

# x = "1"
 
# if x == 1:
#     print("one")
# elif x == "1":
#     if int(x) > 1:
#         print("two")
#     elif int(x) < 1:
#         print("three")
#     else:
#         print("four")
# if int(x) == 1:
#     print("five")
# else:
#     print("six")

# bucle infinito
# while True:
#     print("Estoy atrapado dentro de un bucle.")



# cuanta numeros impares y pares que escribas mientras cierras el ciclo
# odd_numbers = 0
# even_numbers = 0
 
# # Lee el primer número.
# number = int(input("Introduce un número o escribe 0 para detener: "))
 
# # 0 termina la ejecución.
# while number != 0:
#     # Verificar si el número es impar.
#     if number % 2 == 1:
#         # Incrementar el contador de números impares odd_numbers.
#         odd_numbers += 1
#     else:
#         # Incrementar el contador de números pares even_numbers.
#         even_numbers += 1
#     # Leer el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))
 
# # Imprimir resultados.
# print("Conteo de números impares:", odd_numbers)
# print("Conteo de números pares:", even_numbers)

# counter = 5
# while counter != 0:
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)

# secret_number = 777

# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)

# number = int(input("¿Cuál es el número secreto?   "))

# while number != 777:
    
#     print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#     number = int(input("¿Cuál es el número secreto?   "))
    
# print("¡Bien hecho, muggle! Eres libre ahora.")

# print()
# print("While")
# i = 0
# while i < 5:
#     print("El valor de i es", i)
#     i += 1
    
# print()
# print("For")
# for i in range(5):
#     print("El valor de i es", i)
#     pass

# for i in range(2, 8):
#     print("El valor de i es", i)


# power = 1
# for expo in range(16):
#     print("2 a la potencia de", expo, "es", power)
#     power *= 2


# num=2
# for mul in range(11):
#     print(num, "*", mul, "es", (num*mul))
    
# import time

# for i in range(1, 6):
#     print(i, "Mississippi")
#     time.sleep(1)
# print()
# print("¡Listo o no, allá voy!")

# # break - ejemplo

# print("La instrucción break:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")


# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")

# while True:
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")

# largest_number = -99999999
# counter = 0

# number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# while number != -1:
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

# if counter:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")



# secret_tex = "chupacabra"
# while True:
#     text = input("¿Cuál es la palabra secreta?   ")
#     if text == "chupacabra":
#         print("Has dejado el bucle con éxito.")
#         break
#     else:
#         print("¡Estás atrapado jajaj!")



# elimina bocales de palabras y ponerlas de forma vertical

# user_word = input("Ingresa una palabra: ")

# user_word = user_word.upper()

# for letter in user_word:
#     if letter in ['A', 'E', 'I', 'O', 'U']:
#         continue
#     print(letter)


# elimina bocales de palabras y ponerla de forma horizontas

# user_word = input("Ingresa una palabra: ")

# user_word = user_word.upper()

# word_without_vowels = ""

# for letter in user_word:
#     if letter in ['A', 'E', 'I', 'O', 'U']:
#         continue
#     else:
#         word_without_vowels += letter

# print("La palabra sin vocales es:", word_without_vowels)


# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)


# i = 5
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)

# for i in range(5):
#     print(i)
# else:
#     print("else:", i)

# i = 111
# for i in range(2, 1):
#     print(i)
# else:
#     print("else:", i)


# blocks = int(input("Ingrese la cantidad de bloques que tienen los constructores: "))

# height = 0
# total_blocks = 0

# while total_blocks <= blocks:
#     height += 1
#     total_blocks += height

# print("La altura de la pirámide es:", height - 1)

# c0 = int(input("Ingrese un número natural: "))
# steps = 0

# while c0 != 1:
#     print(c0)
#     if c0 % 2 == 0:
#         c0 //= 2
#     else:
#         c0 = 3 * c0 + 1
#     steps += 1

# print(1)  # Imprimir el último valor, que siempre será 1
# print("Pasos =", steps)



# var = 17
# var_right = var >> 1
# var_left = var << 2
# print(var, var_left, var_right)


# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

# numbers[0] = 111
# print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.





# numbers = [10, 5, 7, 2, 1]
# print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

# numbers[0] = 111
# print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

# numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
# print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

# print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

# ###

# del numbers[1]  # Eliminando el segundo elemento de la lista.
# print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
# print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.


# numbers = [1, 2, 3, 4, 5]

# # Paso 1
# numbers[2] = int(input("Ingrese un número para reemplazar al número central: "))

# # Paso 2
# numbers.pop()

# # Paso 3
# print("La longitud de la lista es:", len(numbers))



# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# ###

# numbers.append(4)

# print(len(numbers))
# print(numbers)

# ###

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

# #


# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.append(i + 1)

# print(my_list)


# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#     total += my_list[i]

# print(total)


# my_list = [8, 10, 6, 2, 4]  # lista a ordenar
# swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
# while swapped:
#     swapped = False  # no hay intercambios hasta ahora
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # ¡ocurrió el intercambio!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
# print(my_list)


# my_list = []
# swapped = True
# num = int(input("¿Cuántos elementos deseas ordenar?: "))

# for i in range(num):
#     val = float(input("Ingresa un elemento de la lista: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nOrdenada:")
# print(my_list)

# list_1 = [1]
# list_2 = list_1
# list_1[0] = 2
# print(list_2)


# # Copiando la lista completa.
# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)

# # Copiando parte de la lista.
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)


# my_list = [0, 3, 12, 8, 2]

# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# my_list = [0, 3, 12, 8, 2]

# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)


# # Inicializar el tablero
# board = [['.' for _ in range(8)] for _ in range(8)]

# # Definir las piezas
# ROOK = 'R'
# KNIGHT = 'N'
# PAWN = 'P'

# # Agregar torres
# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK

# # Agregar caballo a C4
# board[4][2] = KNIGHT

# # Agregar peón a E5
# board[3][4] = PAWN

# # Imprimir el tablero
# for row in board:
#     print(" ".join(row))


# Cubo - un arreglo tridimensional (3x3x3)
 
# cube = [[[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':(', 'x', 'x']],
 
#         [[':)', 'x', 'x'],
#          [':(', 'x', 'x'],
#          [':)', 'x', 'x']],
 
#         [[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':)', 'x', 'x']]]
 
# print(cube)
# print(cube[0][0][0])  # output: ':('
# print(cube[2][2][0])  # output: ':)'

# x = 1
# x = x == x
# print(x)

# i = 0
# while i <= 3 :
#     i += 2
#     print("*")

# i = 0
# while i <= 5 :
#     i += 1
#     if i % 2 == 0:
#       break
#     print("*")

# for i in range(1):
#     print("#")
# else:
#     print("#")

# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")

# var = 1
# while var < 10:
#     print("#")
#     var = var << 1

# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)

# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
 
# # print(c + d + e)

# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])

# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])

# vals = [0, 1, 2]
# vals[0], vals[2] = vals[2], vals[0]
# print(vals)
 
# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
# print(vals)

# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]
# print(nums)
# print(vals)

# nums = [1, 2, 3]
# vals = nums[-1:-2]
# print(nums)
# print(vals)

# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)

# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)
 
# my_list = [i for i in range(-1, 2)]
# print(my_list)

# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])