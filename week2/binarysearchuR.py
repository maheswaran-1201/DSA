def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

numbers = [2,6,7,10,15,16,21]
target_val = 16

result = binary_search_recursive(numbers, target_val, 0, len(numbers) - 1)

if result != -1:
    print("Element found at index" , result)
else:
    print("Element not found in array")


