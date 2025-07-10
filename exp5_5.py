input_string = input("Enter a string: ")

input_string = input_string.lower()

alphabet_count = {}

for char in input_string:
    if char.isalpha():  
        if char in alphabet_count:
            alphabet_count[char] += 1
        else:
            alphabet_count[char] = 1

for alphabet, count in alphabet_count.items():
    print(f"{alphabet}: {count}")
