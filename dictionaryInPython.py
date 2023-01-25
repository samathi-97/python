person = {"firstName": "Samathi","age": 23 , "Gender":"female" , "Addres": "Tangalle"}

print(person["firstName"])

print("What you want to know")
key = input()

print(person.get(key))
