def pow(p,n):
    if n==0:
        return 1
    return p*pow(p,n-1)
p=int(input("enter the value of p:"))
n=int(input("enter the value of n:"))
print(pow(p,n))
