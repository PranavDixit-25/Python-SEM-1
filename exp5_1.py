input_string = input("Enter a string: ")

count = 0
for char in input_string:
    if char.isupper():
        count += 1

print(f"The number of capital letters in the given string is: {count}")
