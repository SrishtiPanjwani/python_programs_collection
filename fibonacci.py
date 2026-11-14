# Fibonacci Series Program
terms = int(input("How many terms do you want? "))

if terms <= 0:
    print("Please enter a positive number of terms.")
else:
    first, second = 0, 1
    print("Fibonacci series:")
    for _ in range(terms):
        print(first, end=" ")
        first, second = second, first + second
    print()
