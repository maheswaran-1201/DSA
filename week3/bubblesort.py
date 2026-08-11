def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr = []
z = int(input("Enter the number of elements: "))
for k in range(z):
    arr.append(int(input("Enter the element: ")))
#bubble_arr = arr.copy()
print("Original array:", arr)
print("Sorted array:", bubble_sort(arr))

