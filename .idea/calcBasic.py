try:
    number1 = int(input("podaj pierwszą liczbę: "))

    mat = ""

    while mat != "+" and mat != "-" and mat != "*" and mat != "/":
        print("zły znak działania !")
        mat = input("podaj znak działania: ")

    number2 = int(input("podaj druhą liczbę: "))

    if mat == "+":
        print("wynik to: " + str(number1 + number2))
    elif mat == "-":
        print("wynik to: " + str(number1 - number2))
    elif mat == "*":
        print("wynik to: " + str(number1 * number2))
    elif mat == "/":
        print("wynik to: " + str(number1 / number2))

except ValueError as err:
    print(err)


