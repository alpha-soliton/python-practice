from typing import Any, Sequence

def binary_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr)//2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input('I will binary_search the key value from the list you give.\ninput the number of the element :'))
    x = [None] * num

    print('input the list in ascending order.')

    x[0] = int(input('x[0] : '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i-1]:
                break
    
    ky = int(input('input the key value : '))

    idx = binary_search(x, ky)
    
    if idx == -1:
        print('your value does not exist in the list.')
    else:
        print(f'your value exists in x[{idx}].')
