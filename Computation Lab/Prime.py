#prime numbers
import numpy as np
import time
def remove_element(array,element):
    for i in array:
        if i==element:
            array.remove(element)
    return array
start=time.time()
numbers=[]
no=int(input("Input the number till which u want prime numbers :"))
for i in range(3,no,2):
    numbers.append(i)
prime=[2]
for i in numbers:
    count=0
    for k in range(len(prime)):
        if i%prime[k]==0:
            count=1
    if count==0:
        prime.append(i)
        for number in numbers:
            numbers=remove_element(numbers,i*number)
print("\n prime are:",prime)
end=time.time()
print(end-start)

