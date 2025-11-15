def sum_ending_with_3(numbers):
    total = 0
    for num in numbers:
        if abs(num) % 10 == 3:
            total += num
    return total

nums = [13, 23, 45, 3, 73, 20, 33]

result = sum_ending_with_3(nums)
print("Sum of numbers ending with 3:", result)
print("\nApurva Kumar, 04814902024")