print ("SSSSS")

n = input("what is your name (Put Ash)")
print("hello ", n)
a= 3
b = 4
c = a + b
print (c)
x = int()
x = int(input("What IS X?"))
if x>=10:
    print("x is Ash")
elif x == 0:
    print ("x is not Ash")
else:
    print("x is not big or zero")
fname = input("question:")
age = 0
age = int(input("Age: "))
count = 0
while count <=5:
    print(count)
    count+=1
def greet(firstname):
    print("Hello,", firstname)
greet("Alice")

a = int(input("Name a Number"))
b = int(input("Name A Second Number"))

def add(a,b):
    return a + b
result = add(a,b)
print(result)

minecraftmobs = ["Ghast","Ocelot", "Cat", "Zombie Pigman", "Zombie", "Pigman", "Skelton", "Sheep", "Cow", "Chicken", "Blaze"]
for m in minecraftmobs:
    print(m)
ages = {"Alice": 30, "Bob":25}
print ("Alice's age is",ages["Alice"])
number = int(input("Pick a number greater than 5"))
counting = 5
if number >= 5:
    while number > counting:
        counting+=1
        print(counting)
else:
    print("You Did not enter bigger than 5")
