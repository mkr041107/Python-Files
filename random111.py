import random
highnumber = 1000000
numbs=[]
rnd =random.randint(1, highnumber)
while highnumber > 1:
    rnd = random.randint(1, highnumber)
    if rnd <= highnumber/2:
        highnumber = rnd
        numbs.append(highnumber)
for i in numbs:
    print(i)
    