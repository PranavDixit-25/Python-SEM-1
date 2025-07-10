input_string = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in input_string:
    if char in vowels:
        count += 1

print(f"The total number of vowels in the given string is: {count}")
