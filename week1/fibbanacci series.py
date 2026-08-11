def fibbanacci(n):
    if n<=1:
        return 1
    return fibbanacci(n-1)+ fibbanacci(n-2)
n=int(input("enter the value of n:"))
for i in range(n):
    print(fibbanacci(i),end="")
