#exponets
#java x=2, y=3, z=Math.pow(2,3)
#base = int(input("Enter The Base: "))
#exp = int(input("Exponet: "))
#ans = base**exp
#print(ans)
import math

answer = int(input("1 For Count Up 2 For Counting Down"))
if answer == 1:
    Num = 0
    sum = 0

    while Num <115132219018763992565095597973971522402:
        Num +=1
        digits = [int(digit)for digit in str(Num)]
        length = len(digits)
        for iee in digits:
            sum +=  iee ** length
        if (sum == Num):
            print(sum) 
    
        sum = 0
if answer == 2:
    Num = 5000000
    sum = 0

    while Num >0:
        Num -=1
        digits = [int(digit)for digit in str(Num)]
        length = len(digits)
        for iee in digits:
            sum +=  iee ** length
        if (sum == Num):
            print(sum) 
    
        sum = 0
    
