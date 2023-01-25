data_valid = False
grade1 = 0
grade2 = 0
while data_valid == False:
    grade1 = int(input("add data 1: " ))
    if grade1 < 0 or grade1 > 10:
        print("Wrong data")
        continue
    else:
        print("valid")
        data_valid = True