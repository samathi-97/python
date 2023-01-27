nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

print("using not operator")

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

print(".....Commands....")
commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]
#your code goes here
com = input("Say your command:")
bol = com in commands
#print(com in commands)
if ( bol == True):
    print("OK")
else:
    print("Not supported")   