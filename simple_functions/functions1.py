
__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


def factorial(n):
    return n * factorial(n-1) if n-1 > 0 else 1


print(factorial(4))
