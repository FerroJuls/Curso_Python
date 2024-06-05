# def hi(name):
#     print("Hola,", name)
 
# hi("Greg")

# def hi_all(name_1, name_2):
#     print("Hola,", name_2)
#     print("Hola,", name_1)
 
# hi_all("Sebastián", "Konrad")




# imprimir direccion paciente

# def address(street, city, postal_code):
#     print("Tu dirección es:", street,"St.,", city, postal_code)
 
# s = input("Calle: ")
# p_c = input("Código Postal: ")
# c = input("Ciudad: ")
# address(s, c, p_c)


# # Ejemplo 1
# def subtra(a, b):
#     print(a - b)
 
# subtra(5, 2) # salida: 3
# subtra(2, 5) # salida: -3
 
 
# # Ejemplo 2
# def subtra(a, b):
#     print(a - b)
 
# subtra(a=5, b=2) # salida: 3
# subtra(b=2, a=5) # salida: 3
 
# # Ex. 3
# def subtra(a, b):
#     print(a - b)
 
# subtra(5, b=2) # salida: 3
# subtra(5, 2) # salida: 3


# cambio de nombre al imprimir
# def intro(a="James Bond", b="Bond"):
#     print("Mi nombre es", b + ".", a + ".")
 
# intro(b="Sean Connery")


# def add_numbers(a, b=2, c):
#     print(a + b + c)
 
# add_numbers(a=1, c=3)



# verdadero
# def happy_new_year(wishes = True):
#     print("Tres...")
#     print("Dos...")
#     print("Uno...")
#     if not wishes:
#         return
 
#     print("¡Feliz año nuevo!")
# happy_new_year()
# happy_new_year(False)

# def boring_function():
#     print("'Modo aburrimiento' ON.")
#     return 123
 
# print("¡Esta lección es interesante!")
# boring_function()
# print("Esta lección es aburrida...")


# # cuenta regreciba
# def strange_list_fun(n):
#     strange_list = []
    
#     for i in range(0, n):
#         strange_list.insert(0, i)
    
#     return strange_list

# print(strange_list_fun(11))


# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"-> ",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fallido")


# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year,month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# test_years = [1900, 2000, 2016, 1987]
# test_months = [ 2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr,mo,"-> ",end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fallido")


# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year, month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# def day_of_year(year, month, day):
#     days = 0
#     for m in range(1, month):
#         md = days_in_month(year, m)
#         if md == None:
#             return None
#         days += md
#     md = days_in_month(year, month)
#     if day >= 1 and day <= md:
#         return days + day
#     else:
#         return None

# print(day_of_year(2000, 12, 31))




# def is_prime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()


# def liters_100km_to_miles_gallon(liters):
#     return 235.214583 / liters

# def miles_gallon_to_liters_100km(miles):
#     return 235.214583 / miles

# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))



# # bad
# def hi():
#     return
#     print("¡Hola!")
 
# hi()


# # good
# def hi():
#     print("¡Hola!")
#     return
 
# hi()



# def is_int(data):
#     if type(data) == int:
#         return True
#     elif type(data) == float:
#         return False
 
# print(is_int(5))
# print(is_int(5.0))
# print(is_int("5"))


# def even_num_lst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
 
# print(even_num_lst(11))



# def list_updater(lst):
#     upd_list = []
#     for elem in lst:
#         elem **= 2
#         upd_list.append(elem)
#     return upd_list
 
# foo = [1, 2, 3, 4, 5]
# print(list_updater(foo))






# def my_function():
#     print("¿Conozco a la variable?", var)


# var = 1
# my_function()
# print(var)


# def my_function():
#     var = 2
#     print("¿Conozco a la variable?", var)
 
 
# var = 1
# my_function()
# print(var)


# def my_function():
#     global var
#     var = 2
#     print("¿Conozco a aquella variable?", var)


# var = 1
# my_function()
# print(var)

# global a hace que todos tengan este mismo numero aunque no esten en la funcion


# def bmi(weight, height):
#     return weight / height ** 2
 
 
# print(bmi(52.5, 1.65))


# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
 
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
 
 
 
 
 
 
# for n in range(1, 6): # probando
#     print(n, factorial_function(n))

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
 
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
 
 
# for n in range(1, 10): # probando
#     print(n, "->", fib(n))


# def fib(n):
#     if n < 1:
#          return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum


# for n in range(1, 10):
#     print(n, "->", fib(n))





# # tupla
# my_tuple = (1, 10, 100, 1000)

# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])

# for elem in my_tuple:
#     print(elem)


# my_tuple = (1, 10, 100)

# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)


# dictionary = {"gato": "cat", "perro": "chien", "caballo": "cheval"}
# phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
# empty_dictionary = {}

# print(dictionary['gato'])
# print(phone_numbers['Suzy'])


# school_class = {}

# while True:
#     name = input("Ingresa el nombre del estudiante: ")
#     if name == '':
#         break
    
#     score = int(input("Ingresa la calificación del estudiante (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)


# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)

# print(duplicates) 



# # unir 
# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)

# print(d3)





# my_list = ["car", "Ford", "flower", "Tulip"]

# t = tuple(my_list)
# print(t)



# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colors_dictionary = dict(colors)
# print(colors_dictionary)



# # saber el rgb del color
# colors = {
#     "blanco": (255, 255, 255),
#     "gris": (128, 128, 128),
#     "rojo": (255, 0, 0),
#     "verde": (0, 128, 0)
#     }
 
# for col, rgb in colors.items():
#     print(col, ":", rgb)


# value = int(input('Ingresa un número natural: '))
# print('El recíproco de', value, 'es', 1/value)



# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x - 1)
 
 
# print(f(3))


# def fun(x):
#     x += 1
#     return x
 
 
# x = 2
# x = fun(x + 1)
# print(x)


# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']
 
# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )
 
# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(k[0])


# def func(a, b):
#     return a ** a
 
 
# print(func(2))


# def func_1(a):
#     return a ** a
 
 
# def func_2(a):
#     return func_1(a) * func_1(a)
 
 
# print(func_2(2))

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return
 
 
# print(fun(fun(2)) + 1)

# def fun(x):
#     global y
#     y = x * x
#     return y
 
 
# fun(2)
# print(y)

# def any():
#     print(var + 1, end='')
 
 
# var = 1
# any()
# print(var)




# def fun(x, y, z):
#     return x + 2 * y + 3 * z
 
 
# print(fun(0, z=1, y=3))


# def fun(inp=2, out=3):
#     return inp * out
 
 
# print(fun(out=2))

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']
 
# for k in range(len(dictionary)):
#     v = dictionary[v]
 
# print(v)


# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# try:
#     value = input("Ingresa un valor: ")
#     print(value/value)
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada errónea...")
# except TypeError:
#     print("Entrada muy errónea...")
# except:
#     print("¡Buuu!")

# my_list = [1, 2]
 
# for v in range(2):
#     my_list.insert(-1, my_list[v])
 
# print(my_list)

# nums = [1, 2, 3]
# vals = nums

# def function_1(a):
#     return None
 
 
# def function_2(a):
#     return function_1(a) * function_1(a)
 
 
# print(function_2(2))

# def func(a, b):
#     return b ** a
 
 
# print(func(b=2, 2))

# z = 0
# y = 10
# x = y < z and z > y or y < z and z < y

# print(x)

# my_list = [x * x for x in range(5)]
 
 
# def fun(lst):
#     del lst[lst[2]]
#     return lst
 
 
# print(fun(my_list))

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z
 
# print(x, y, z)

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b
 
# print(a, b)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
 
 
# print(fun(fun(2)))


# nums = [1, 2, 3]
# vals = nums
# del vals[:]

# # print(vals)

# y="3"
# x="6"

# print(x + y)

# print("a", "b", "c", sep="sep")


# x = 1 // 5 + 1 / 5
# print(x)

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']
 
# for k in range(len(dct)):
#     v = dct[v]
 
# print(v)


# lst = [i for i in range(-1, -2)]
# print(lst)

# def fun(a, b, c=0):
    
#     fun(b=0, a=0)
# print(fun)


# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)
 
 
# print(fun(0, 3))


# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")
 
 
# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)

# dd = {"1": "0", "0": "1"}
# for x in dd.vals():
#     print(x, end="")

# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)
 
# for x in dct.keys():
#     print(dct[x][1], end="")

# def fun(inp=2, out=3):
#     return inp * out
 
 
# print(fun(out=2))


# lst = [[x for x in range(3)] for y in range(3)]
 
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")

# try:
#     value = input("Ingresa un valor: ")
#     print(int(value)/len(value))
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada erronea...")
# except TypeError:
#     print("Entrada muy erronea...")
# except:
#     print("¡Buuu!")


# try:
#     print(5/0)
#     break
# except:
#     print("Lo siento, algo salió mal...")
# except (ValueError, ZeroDivisionError):
#     print("Mala suerte...")


# foo = (1, 2, 3)
# foo.index(0)