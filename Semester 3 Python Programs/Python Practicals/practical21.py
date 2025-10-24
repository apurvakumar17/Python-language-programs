import math
num = float(input("Enter a number: "))

print("\n=== Basic Math Functions ===")
print("Absolute value:", abs(num))
print("Ceiling value:", math.ceil(num)) 
print("Floor value:", math.floor(num)) 
print("Square root:", math.sqrt(num) if num >= 0 else "Not defined for negative numbers")
print("Exponential (e^num):", math.exp(num))
print("Power (num^2):", math.pow(num, 2))
print("Logarithm (base e):", math.log(num) if num > 0 else "Not defined for ≤ 0")
print("Logarithm (base 10):", math.log10(num) if num > 0 else "Not defined for ≤ 0")

print("\n=== Trigonometric Functions (input in radians) ===")
angle_rad = float(input("Enter an angle in radians: "))
print("sin(angle):", math.sin(angle_rad))
print("cos(angle):", math.cos(angle_rad))
print("tan(angle):", math.tan(angle_rad))
print("arcsin(0.5):", math.asin(0.5))
print("arccos(0.5):", math.acos(0.5))
print("arctan(1):", math.atan(1))

print("\n=== Constants ===")
print("Value of pi:", math.pi)
print("Value of e:", math.e)

print("\nApurva Kumar, 04814902024")