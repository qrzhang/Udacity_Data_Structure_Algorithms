"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""


def get_fib_seq(position):
    first = 0
    second = 1
    third = first + second
    seq = [first, second, third]

    if position < 1:
        return -1
    elif position < 4:
        return seq[:position - 1]
    else:
        for i in range(3, position):
            first = second
            second = third
            third = first + second
            seq.append(third)
            i += 1
        return seq


def my_get_fib(position):
    first = 0
    second = 1
    third = first + second

    if position < 0:
        return -1
    elif position == 0:
        return first
    elif position == 1:
        return second
    elif position == 2:
        return third
    else:
        for i in range(2, position):
            first = second
            second = third
            third = first + second
        return third


def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
