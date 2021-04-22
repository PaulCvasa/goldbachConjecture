n=int(input("n(even number)= "))

def prime(x):
    while x:
        if x<2:
            return 0
        if x%2==0 and x!=2:
            return 0
        for i in range(3,x//2,2):
            if x%i==0:
                return 0
        return 1

def anomaly_finder(x):
    startNumber=x
    found=0
    while(x):
        if(prime(x)):
            last_primeNumber=x
            pair_of_theSum=startNumber-last_primeNumber
            if prime(pair_of_theSum):
                print("For number ",startNumber,"the sum is made of ",last_primeNumber," and ",pair_of_theSum)
                found=1
                break
            else:
                x-=1
        else:
            x-=1
    if found==0:
        print("!!! NO PAIR OF NUMBERS FOUND FOR ",startNumber,"!!!")
    
for i in range(n,2,-2):
    anomaly_finder(i)
    
