def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low = mid+1
        else:
            high = mid-1
    return -1
n = int (input("enter number of elements:"))
arr = []
print("enter the elements:")
for i in range(n):
    arr.append(int(input()))
key = int(input("enter the element to search"))
result = binary_search(arr,key)
if result != -1:
    print("element found at index", result)
else:
    print("element not found in the array")