def binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers)
target = int(input("Enter the number to search: "))

result = binary_search(numbers, 0, len(numbers) - 1, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found.")
print("\nApurva Kumar, 04814902024")