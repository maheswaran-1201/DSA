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
a = list(map(int, input("Enter numbers to sort: ").split()))
n = len(a)
quicksort(a, 0, n - 1)
print("Sorted array:")
print(a)
