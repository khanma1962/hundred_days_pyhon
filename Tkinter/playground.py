def add(*args):
    print(f"Arg is type {type(args)}")
    total = 0
    for n in args:
        total += n
    return total


print(add(8, 10, 9, 3, 2, 9999, 10000, 99))


def calculator(n, **kwargs):
    print(f"kwarg is {(kwargs)}")
    print(f"kwarg type is {type(kwargs)}")
    n += kwargs['add']
    n *= kwargs['mul']
    return n


print(calculator(6, add=5, mul=9))
