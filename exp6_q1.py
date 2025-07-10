n = int(input())
values = [int(input()) for _ in range(n)]
counts = {i: 0 for i in range(4)}
for value in values:
    if 0 <= value <= 3:
        counts[value] += 1
for value, count in counts.items():
    print(value, count)
