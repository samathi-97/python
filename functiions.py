
# this is a function
def say_hello():
    print("Hello")

def say_hi(person):
    print("Hello " + person + ", have a niceday")

def far2Cel(far):
    celcius = (5*(far-32))/9
    return celcius

#calling function
say_hello()
say_hi("samathi")    

print("celcius :-" , round(far2Cel(100),2))

