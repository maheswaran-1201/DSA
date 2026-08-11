def fact(n):
    if n == 0 | n == 1:
        return 1
    return n* fact(n-1)
n= int (input("enter the value:"))
print(fact(n))
