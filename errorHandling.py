number = input("Type a number:")

try:
    number = float(number)
    print("number is :" ,number)

except:
    print("Invalid Number")