# recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
print(fact(6))  # Output: 720

