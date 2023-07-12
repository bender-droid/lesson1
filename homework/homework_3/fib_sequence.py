def fib(end):
    start_sequence = [0, 1]
    current_number = 0
    while current_number < end:
        current_number = start_sequence[-1] + start_sequence[-2]
        start_sequence.append(current_number)
    print(f'Последовательность: {", ".join(map(str, start_sequence[1:]))}')


fib(89)
