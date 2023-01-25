#list and tuples in python
print ("enter your b day in format DD-MM-YYY")
birthday = input() 
print(birthday)

monthsOfYear = ("jan","Feb","March","April","May")

monthIndex = int(birthday[3:5]) - 1
print(monthIndex)

nameOfMonth = monthsOfYear[monthIndex]

print(nameOfMonth)