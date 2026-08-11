def search(i):
    l=[1001,1002,1003,1004,1005]
    for j in range(len(l)):
        if l[j]==i:
            return j,i
    return search(i)

i = int(input("enter the id to be searched:"))      
print(search(i))
