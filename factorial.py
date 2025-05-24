# Function to compute factorial with working steps
def factorial(n):
    result = 1
    print(f"Calculating {n}!")
    for i in range(1, n + 1):
        result *= i
        print(f"Step {i}: {i}! = {result}")
    return result

# Number to find factorial of
number = 5
fact = factorial(number)
print(f"\nThe factorial of {number} is {fact}")

