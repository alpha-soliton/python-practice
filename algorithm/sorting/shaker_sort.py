from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last
        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                last = j
        right = last


if __name__ == '__main__':
    print('simple sorting algorithm: shaker_sort')
    num = int(input('num of element : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    shaker_sort(x)

    print('sorted in ascending order.')
    for i in range(num):
        print(f'x[{i}] : {x[i]}')
