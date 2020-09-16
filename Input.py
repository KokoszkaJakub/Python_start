listofUsers = []

i = 1

while i <= 2:
    Name = input("hello, give me your name: ")
    SName = input("and your surname ? ")
    print("hello " + Name + " " + SName)
    mail = input("we need more info " + Name + ", what your email adress? ")
    i = i + 1
    user1 = "user: " + Name + " " + SName + ", email: " + mail
    listofUsers.append(user1)

print(listofUsers)
