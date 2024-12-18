# app.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

if __name__ == "__main__":
    num1 = 10
    num2 = 5

    print(f"Addition of {num1} and {num2}: {add(num1, num2)}")
    print(f"Subtraction of {num1} and {num2}: {subtract(num1, num2)}")
    print(f"Multiplication of {num1} and {num2}: {multiply(num1, num2)}")
    print(f"Division of {num1} by {num2}: {divide(num1, num2)}")
