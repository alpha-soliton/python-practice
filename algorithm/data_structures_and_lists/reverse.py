from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    # reverse the order of the mutable sequence
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('this function reverse the order of the list')
    nx = int(input('what is the number of the list : '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}] : '))

    reverse_array(x)

    print('I reversed the order of the list.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')

