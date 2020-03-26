from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

if __name__ == '__main__':
    print('simplest sorting algorithm: bubble_sort')
    num = int(input('num of element : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort(x)

    print('sorted in ascending order.')
    for i in range(num):
        print(f'x[{i}] : {x[i]}')
