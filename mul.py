class multiplication:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Creating an object of the class
mul = multiplication(num1, num2)

# Displaying the result
print(f"The sum of {num1} and {num2} is: {mul.add()}")
