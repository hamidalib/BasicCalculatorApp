# A basic calculator application for performing simple Arithmetic operation.

Num_One = int(input("Enter first number here: "))
Num_Two = int(input("Enter second number here: "))
Operation = input("Enter the operation you want to perform on your numbers (+, -, *, /): ")

if Operation == "+":
    result = Num_One + Num_Two
elif Operation == "-":
    result = Num_One - Num_Two
elif Operation == "*":
    result = Num_One * Num_Two
elif Operation == "/":
    result = Num_One / Num_Two
else:
    print("Invalid Operation! You can only perform these operations: +, -, *, /")
print(result)