class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."


calculator = Calculator()
a = float(input("enter the first number : "))
b = float(input("enter the second number : "))
operation = str(input("enter the operation : "))

if operation == "+":
    result = calculator.add(a, b)
elif operation == "-":
    result = calculator.subtract(a, b)
elif operation == "*":
    result = calculator.multiply(a, b)
elif operation == "/":
    result = calculator.divide(a, b)
else:
    result = "Invalid operation"

print(f"The result of the operation is: {result}")
