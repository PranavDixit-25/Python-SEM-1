def fib(n):
    series = [0, 1]
    while len(series) < n:
        next_val = series[-1] + series[-2]
        series.append(next_val)
    return series

num_terms = 10
fib_series = fib(num_terms)
print(f"Fibonacci series up to {num_terms} terms: {fib_series}")
