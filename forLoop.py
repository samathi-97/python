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