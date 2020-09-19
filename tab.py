# excel
#
#

numberGrid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# print(numberGrid[0][0])
# print(numberGrid[1][1])
# print(numberGrid[3][0])

for row in numberGrid:
    print(row)

for row2 in numberGrid:
    for column in row2:
        print(column)

employeeList = [
    ["lp", "name","sName", "number", "mail"],
    [1, "Adam", "Kovalsky", 606123321, "akov@o2.pl"],
    [2, "bob", "Smith", 701234473, "bob@smith.com"],
    [3, "Stev", "Inch", 888123999, "inch_S@azureus.com"]

]
print(employeeList[1][1])

for tab in employeeList:
    print(tab)

for tab2 in employeeList:
    for all in tab2:
        print(all)
