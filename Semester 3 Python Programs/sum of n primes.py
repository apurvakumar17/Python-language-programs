def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
num = 2
sum = 0

n = int(input("Enter: ")) 
while count != n:
    if is_prime(num):
        sum += num
        count+=1
    num+=1 
print(sum)