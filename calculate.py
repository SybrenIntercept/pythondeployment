class CustomCalculator:
    @staticmethod
    def calculate(a, b):
        print(f"Add:      {a} + {b} = {a + b}")
        print(f"Subtract: {a} - {b} = {a - b}")
        print(f"Multiply: {a} * {b} = {a * b}")
        print(f"Divide:   {a} / {b} = {a / b}" if b != 0 else "Divide:   division by zero")
        return a+b

CustomCalculator.calculate(10, 2)
