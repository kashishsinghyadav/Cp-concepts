import math 
# Time complexity = o(sqrt(n))
# space complexity = o(1)
def findprime(n):
    # all prime can be expressed in 6n+1 or 6n-1
    if n<=1:# 1 is niether prime nor composite 
        return False
    if n<=3:
        return True
        
    for i in range(5,int(math.sqrt(n))+1,6):
        if i%n==0 or (i+2)%n==0:
            return False
    return True
n=int(input('enter the number'))
print(findprime(n))

    
    
