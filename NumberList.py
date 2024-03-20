#main
from MyFunctions import Numberss
import statistics
odd = []
even = []
print1 = []
total = 0
total1 = 0
addlist=0
addlist1=0
r1= int(input("List a number from 1 to 10000"))
r2 = r1 + 10000
listadd = Numberss()
while r2 >= r1:
    print1.append(r1)
    r1+=1
for e in print1:
    if e% 2 ==0:
        even.append(e)
    else:
        odd.append(e)
addlist = 0
for i in odd:
    total = i+addlist
    addlist = total
for t in even:
    total1 = t+addlist1
    addlist1 = total1
print("Sum of Odds:", '{:,.2f}'.format(total))
print("Sum of Evens:", '{:,.2f}'.format(total1))
mean1 = statistics.mean(even)
median1 = statistics.median(even)
mode1 = statistics.mode(even)
mean = statistics.mean(odd)
median = statistics.median(odd)
mode = statistics.mode(odd)
print("Mean of Odds:", '{:,.2f}'.format(mean))
print("Median of Odds:", '{:,.2f}'.format(median))
print("Mode of Odds:", '{:,.2f}'.format(mode))
print("Mean of Evens:", '{:,.2f}'.format(mean1))
print("Median of Evens:", '{:,.2f}'.format(median1))
print("Mode of Evens:", '{:,.2f}'.format(mode1))

    