def fibonacci_sequence(n):
    fib_seq = [1, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

term = int(input("Enter the number of terms for Fibonacci sequence: "))
print(*fibonacci_sequence(term))
