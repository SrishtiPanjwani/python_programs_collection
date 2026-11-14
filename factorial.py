# Factorial Program
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(f"Factorial of {number} is {result}")
