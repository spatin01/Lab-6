#Samantha Patin and Therese Burns
n=input("Enter positive integer:\n")
n=int(n)

def fibonacci (n):
    if n==0:
        return n
    elif n==1:
        return n
 
    else:
        sum=fibonacci(n-2)+fibonacci(n-1)
    return sum
print(fibonacci(n))
