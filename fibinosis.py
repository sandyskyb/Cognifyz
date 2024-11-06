def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Generate Fibonacci sequence up to the 10th term
fibonacci_sequence(10)

