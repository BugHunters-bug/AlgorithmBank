from math import *

def find_divisor1(n):
    #time_complexity= O(n)
    result=[]
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)
    return result   

def find_divisor2(n):
    #Time_complexity=O(sqrt(n))
    result_set=set()
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            result_set.add(i)
            result_set.add(n//i)
    return result_set

    







t=int(input())
while t:
    n=int(input())
    result=find_divisor1(n)
    result_set=find_divisor2(n)
    
    t-1
    print(*result)
    print(*result_set)
