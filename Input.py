Name = input("hello, give me your name: ")

print("hello " + Name)

age = int(input("how old are you ? "))


def printHello():
    print("you are " + str(age) + " years old")


if 99 > age >= 18:
    printHello()
    print("jesteś pelnoletni")

elif age > 100:
    print("you are dead")

elif age < 0:
    print("error ")


else:
    print("jestes jeszcze dzickiem")
    printHello()
