def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr = []
z = int(input("Enter the number of elements: "))
for k in range(z):
    arr.append(int(input("Enter the element: ")))
arr = arr.copy()
print("Original array:", arr)
print("sorted array:", insertion_sort(arr))
