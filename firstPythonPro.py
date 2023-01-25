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

#while loop in python

i = 1
while i <=5:
   print(i)
   i = i + 1

print("Finished!")    

#program to use while with if else
turn = 0
points = 100

while turn<4:
    print("enter hit or miss")
    txt = input()
    if txt == 'hit':
        points = points+10
        turn = turn+1
    else:
         points = points - 20
         turn = turn +1

print(points)     


# code to calculate ticket price with continue
total = 0
noOfPassengers = 0

while noOfPassengers <5:
    ageofPassenger = int(input())
    noOfPassengers +=1
    if ageofPassenger < 3 :
        continue 
    else:
        total = total+100
print (total)            

