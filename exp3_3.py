number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    print(f"The greatest number is {number1}.")
elif number2 > number1:
    print(f"The greatest number is {number2}.")
else:
    print("The numbers are equal.")
