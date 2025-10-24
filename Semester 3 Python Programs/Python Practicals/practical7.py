def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

print("Number of vowels in \"Hello World\" : ", count_vowels("Hello World"))

print("\nApurva Kumar, 04814902024")