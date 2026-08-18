def linear_search(arr,key):
    for i in range (len(arr)):
        if arr[i] == key:
            return i
    return -1

n = int (input("enter number of elements:"))
arr = []
print("enter the elements:")
for i in range(n):
    arr.append(int(input()))
key = int(input("enter the element to search"))
result = linear_search(arr,key)
if result != -1:
    print("element found at index", result)
else:
    print("element not found in the array") 

