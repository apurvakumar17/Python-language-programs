def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1           

numbers = [10, 23, 45, 70, 11, 15]
print(numbers)
target = int(input("Enter the number to search: "))

result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list.")
print("\nApurva Kumar, 04814902024")