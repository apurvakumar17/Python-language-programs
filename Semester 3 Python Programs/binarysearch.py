def binarysearch(start,end,arr,target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binarysearch(start, mid-1, arr, target)
    elif arr[mid] < target:
        return binarysearch(mid+1, end, arr, target)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    tr = int(input("Enter the number to search: "))
    res = binarysearch(0, len(arr)-1, arr, tr)
    if res == -1:
        print("Entered element not found!")
    else:
        print (f"Element found at {res} !")
        