def binary_search(arr, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        print(mid)
        return mid
    elif target < arr[mid]:
        return binary_search(arr, start, mid - 1, target)
    elif target > arr[mid]:
        return binary_search(arr, mid + 1, end, target)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    tr = int(input("Enter the number to search: "))
    res = binary_search(arr, 0, len(arr) - 1, tr)
    if res == -1:
        print("Entered element not found!")
    else:
        print (f"Element found at {res} !")