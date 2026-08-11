def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = []
z = int(input("Enter the number of elements: "))
for k in range(z):
    arr.append(int(input("Enter the element: ")))
print("Sorted array:", selection_sort(arr))

























