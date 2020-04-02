from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)

    for i in range(n - 1):
        exchng = 0
        for j in range(n - 1, i, -1):
            if a[j -1] > a[j]:
                a[j - 1], a[j] = a[j], a[j-1]
                exchng += 1
        if exchng == 0:
            break

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last

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
