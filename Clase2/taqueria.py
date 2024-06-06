Menu = {
    "BAJA TACO": 4.00,
    "BURRITO": 7.50,
    "BOW1": 8.50,
    "NACHOS": 11.00,
    "QUESADILLA": 9.50,
    "SUPER BURRITO": 8.50,
    "SUPER QUESADILLA": 9.50,
    "TACO": 3.00,
    "TORTILLA SALAD": 8.00
}

def main():
    orden_total = 0
    while True:
        try:
            item = input("Ingrese artículo de su pedido (o escriba CONTROL-D para finalizar): ").upper()
        except EOFError:
            break
        if item in Menu:
            orden_total += Menu[item]
        elif item == "CONTROL-D":
            print(f"El total de su pedido es ${orden_total:.2f}")
            break
        else:
            print("Artículo inválido")

if __name__ == "__main__":
    main()

