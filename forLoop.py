words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")

letters = ['a', 'b', 'c']

for l in letters:
  print(l+"*")  

str = "testing for loops"
count = 0

for x in str:
  if(x == 't'):
    count += 1

print("No of t in string is :",count) 

numbers = list(range(5))
print(numbers)

numbersN = list(range(3, 8))
print(numbersN)

print(range(20) == range(0, 20))

numbersM = list(range(5, 20, 2))
print(numbersM)

numbersP = list(range(20,5,-2))
print(numbersP)

#List Slices
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

#If the first number in a slice is omitted, it’s taken to be the start of the list.
#If the second number is omitted, it’s taken to be the end.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

#Third Number representing the step
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

str = input("Input a String: ")
print(str[::-1])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

for i in range(10):
  if not i % 2 == 0:
    print(i+1)

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)