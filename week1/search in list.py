def search(i):
    l=[1001,1002,1003,1004,1005]
    for j in range(len(l)):
        if l[j]==i:
            return j,i
        else:
            return("emp id not found")
    return search(i)

i = int(input("enter the id to be searched:"))      
print(search(i))
