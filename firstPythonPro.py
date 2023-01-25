print(5+6)
# if else in python
x = 4
if x == 5:
   print("Yes")
else:
   print("No")
# shorthanf if/else -> elif
num = 3
if num == 1:
  print("One")
elif num == 2:
  print("Two")
elif num == 3: 
  print("Three")
else: 
  print("Something else")

# code to finf leap year or not
print("Enter any year")
year = int(input())

if year%4 != 0 :
    print("not a leap year")
elif year % 100 !=0:
    print("Leap year")
elif year % 400 == 0 :   
    print("Leap year")
elif year % 400 !=0:
    print("not a leap year")
    