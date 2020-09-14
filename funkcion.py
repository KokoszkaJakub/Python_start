def sayHi():
    print("Hello user")


sayHi()


def sayHi2(name):
    print("Hello " + name)


sayHi2("Mike")
sayHi2("Tom")




def dwa(imie, nazwisko, age):
    print("hello " + imie + " " + nazwisko +
          " you are " + str(age) + " years old")

imie1 = input("what your name ? ")
nazwisko1 = input("nazwisko: ")
wiek = input("wiek: ")

dwa(imie1, nazwisko1, wiek)




def cube (num):
    return num * num * num


print(cube(2))