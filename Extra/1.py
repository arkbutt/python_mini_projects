class Math:

    def evenNum(n):
        print("Even NUmbers:"),
        for i in range(n):
            if not(i%2):
                print(i)

    def oddNum(n):
        print("Odd NUmbers:"),
        for i in range(n):
            if(i%2):
                print(i)
    def is_prime(n):
            for i in range(2,n):
                if(n%i==0):
                    return False
            return True

    def primeNum(n):
        print("Prime NUmbers:")
        for i in range(2,n):
            if(Math.is_prime(i)):
                print(str(i) + " , "),
                
   

def nth_odd(n):
    return (n*2)-1
    

def fab(i):
    if (i==0):
        return 0
    elif (i==1):
        return 1
    else:
        return fab(i-1) +fab(i-2)


def triangle(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*nth_odd(i))
        
for i in range(20):
    print(fab(i))
