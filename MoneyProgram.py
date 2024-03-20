import random
import math
#random variable

pc=["50$","20$","10$","5$","1$","Quarter", "Dime", "Nickle", "Penny"]
combined = float(input("Amount: "))
#money vars
Bills=[50.0,25.0,10.0,5.0,1.0,0.25,0.10,0.05,0.01]
many=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
#for loop
for i in range(0,len(Bills)):
  c = int(math.floor(combined/Bills[i]))
  many[i]=c
  combined-=c*Bills[i]
for i in range(0,len(pc)):
  if many[i]>0:
    print(f"{many[i]} - {pc[i]}")
  


         