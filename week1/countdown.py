def countdown(n):
    if n==1:
        return "LAUNCH"
    return  countdown(n-1)

n=int(input("enter the value of n:"))
print(countdown(n))
