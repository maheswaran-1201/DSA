def quicksort(a, low, high):
    if low < high:
        i = low + 1
        j = high
        pivot = low
        while i <= j:
            while i <= high and a[i] <= a[pivot]:
                i += 1
            while j >= low and a[j] > a[pivot]:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
        a[pivot], a[j] = a[j], a[pivot]
        quicksort(a, low, j - 1)
        quicksort(a, j + 1, high)
n = int(input("enter the number of elements"))
a=[]
for i in range(n):
    k=int(input("enter the element"))
    a.append(k)
quicksort(a, 0, n - 1)
print("Sorted array:")
print(a)
