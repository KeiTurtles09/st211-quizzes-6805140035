
def is_even(n):
    return n % 2 == 0

def  factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):   #multiply all integers from 2 to n
        result *= i
    return result