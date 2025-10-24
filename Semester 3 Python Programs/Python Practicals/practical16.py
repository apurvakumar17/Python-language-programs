def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter how many prime numbers to sum: "))

count = 0     # Count of primes found
num = 2       # Starting number
total = 0     # Sum of primes

while count < n:
    if is_prime(num):
        total += num
        count += 1
    num += 1

print("Sum of first", n, "prime numbers is:", total)

print("\nApurva Kumar, 04814902024")