def sum3(arr):
    sum = 0
    for i in arr:
        if abs(i) % 10 == 3:
            sum += i
    return sum


nums = [13, 23, 45, 3, 73, 20, 33]
print(sum3(nums))