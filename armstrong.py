def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_powers = sum(int(digit) ** num_len for digit in num_str)
    return num == sum_powers

for num in range(1, 10000):
    if is_armstrong(num):
        print(num)
