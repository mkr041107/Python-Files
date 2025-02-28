import time
import sys
import logging
num = 3
inum = 3
steps = 0
startt = time.time()
nums = []
numsnumlist = []
numsnum = 0
sequencenums = 0
fin = True
logging.basicConfig(filename='output.log', level=logging.INFO)

while sequencenums < 1000:  
    while num != 1:
     steps += 1
     if num % 2==0:
        num = num/2
     else: 
      num = num * 3+1
     nums.append(num)
     
    
    inum += 1
    num = inum
    numsnum = len(nums)
    sequencenums += 1
    numsnumlist.append(numsnum)
    print(f"\n Biggest Number Is {numsnum}")
    print (f"\n {inum}")
    nums.clear()


    


    steps = 0

ms = (time.time() - startt) * 1000
msrounded =round(ms)
print(f"\nBigest Number Of All {max(numsnumlist)}")
logging.info(f"\nBigest Number Of All {max(numsnumlist)}")
logging.info(f"\n Final Time In Miliseconds: {msrounded}")

   
   
    

    
