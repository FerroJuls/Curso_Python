print("La Witsi Witsi Araña \n subió a su telaraña.")
print()
print("Vino la lluvia \n y se la llevó.")

print()
print()

print("La Witsi Witsi Araña\\subió a  su telaraña.")
print()
print("Vino la lluvia\\ay se la  llevó.")

print()
print()

palabra="subio"
print("La Witsi Witsi Araña" , palabra , "a su telaraña.")

print()
print()

print("Mi nombre es", "Python.")
print("Monty Python.")

print()
print()



print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

print()
print()

print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

print()
print()

print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print()
print()

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

print()
print()
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

print()
print()


# Sample Solution

###################
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)


print()
print()
print("H", "E", "L", "L", "O", sep="-")


print()
print()
print("Mi\nnombre\nes\nBond.", end=" ")
print("James Bond.")


print()
print()
#print(sep="&", "fish", "chips")
print("fish ", " chips",sep="&")

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")


print()


print(0o123)
print(0x123)
print("Me gusta \"Monty Python\"")
print('Me gusta "Monty Python"')
print('I\'m Monty Python.')
print("I'm Monty Python.")


print()
print(3 > 4)
print(1 < 2)


print()

print(2+2)


print("eee")
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print(-4 + 4)
print(-4. + 8)

print(-4 - 4)
print(4. - 8)
print(-1.1)

print(+2)
print(-2)

print(2 + 3 * 5)

print(9 % 6 % 2)
print(9 % 6 )
print( 6 % 2)
print("sss")
print(6 % 2 % 9)

print((2 % -4), (2 % 4), (2 ** 3 ** 2))

print("sss")
a=2
b=3
c=2
r=(a**b)
print (r)
t=(r**c)
print (t)



print()
print()
print()
juan=3
maria=5
adan=6

print("Cantidad manzanas de:")
print("Juan:",juan,"\nAdan:",adan,"\nMaria:",maria)

total_apples=juan+maria+adan
print("Total de manzanas:",total_apples)

print()
print()
print()
x=1
x = x * 2
x = x * 2
x = x * 2
print(x)


b = 3
b *= 2 
print(b)

print()
print()
kilometers = 12.25
miles = 7.38

calcular_km=miles*1.61
calcular_m=kilometers/1.62

print(miles, "millas son",calcular_km , "kilómetros")
print(kilometers, "kilómetros son",calcular_m , "millas")

print()
print()
x =  2
x = float(x)
print("x =", x)

print()
print()
var = 2
var = 3
print(var)

a = '1'
b = "1"
print(a + b)

a = 6
b = 3
a /= 2 * b
print(a)

# print("Dime lo que sea...")
# anything = input()
# print("Hmm...", anything, "... ¿en serio?")


# anything = float(input("Ingresa un número: "))
# something = anything ** 2.0
# print(anything, "a la potencia de 2 es", something)

# leg_a = float(input("Ingresa la longitud del primer cateto: "))
# leg_b = float(input("Ingresa la longitud del segundo cateto: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("La longitud de la hipotenusa es:", hypo)

# leg_a = float(input("Ingresa la longitud del primer cateto: "))
# leg_b = float(input("Ingresa la longitud del segundo cateto: "))
# print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)
 
# fnam = input("¿Me puedes dar tu nombre por favor? ")
# lnam = input("¿Me puedes dar tu apellido por favor? ")
# print("Gracias. ")
# print("\nTu nombre es " + fnam + " " + lnam + ".")

# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")

# leg_a = float(input("Ingresa la longitud del primer cateto: "))
# leg_b = float(input("Ingresa la longitud del segundo cateto: "))
# print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))


print(1//2*3) 
x = 1
y = 2
z = x
x = y
y = z
print(x, y)

x = input(2)
y = input(4)
print(x + y)

print("ASDUIJD")
x = int(input(2))
y = int(input(4))
 
x = x // y
y = y // x
 
print(y)