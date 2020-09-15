Name = input("hello, give me your name: ")
SName = input("and your surname ? ")
print("hello " + Name + " " + SName)
mail = input("we need more info, what your email adress? ")

age = int(input("how old are you ? "))

listOfNames = []
listOfSurname = []
listofMail = []
listofUsers = []

user1 = "user: " + Name + " " + SName + ", email: " + mail

listOfNames.append(Name)
listOfSurname.append(SName)
listofMail.append(mail)
listofUsers.append(user1)

print(listOfNames + listOfSurname + listofMail)
print()
print(listofUsers)

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
