n = int(input())
numbers = tuple(float(input()) for _ in range(n))
average = sum(numbers) / len(numbers)
print(average)
