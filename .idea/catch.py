

try:

    number = int(input("enter a number: "))
    print("your number is: " + str(number))

except ValueError as err:
    print("warning error")
    print(err)
#except ZeroDivisionError:
#    print("divided by 0 !")




