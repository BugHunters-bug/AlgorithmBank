def gcd(a,b):
    #euclid's algorithm time complexity O(log(min(a,b)))
    if a<b:
        return gcd(b,a)
        
    if b==0:
        return a
    return gcd(b,a%b)

    
def lcm(a,b):
    #product_of_num=product(gcd *lcm)

    prod=a*b
    return prod//gcd(a,b)





t=int(input())
while t:
    # a=int(input())
    # b=int(input())
    a,b=map(int,input().split())
    print("gcd= {} lcm= {}".format(gcd(a,b), lcm(a,b)))
    t=t-1