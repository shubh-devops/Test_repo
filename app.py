# app.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

if __name__ == "__main__":
    print("Addition of 10 and 5:", add(10, 5))
    print("Subtraction of 10 and 5:", subtract(10, 5))
    print("Multiplication of 10 and 5:", multiply(10, 5))
    print("Division of 10 by 5:", divide(10, 5))
