from typing import Any, Sequence
import copy

def sentinel_search(seq: Sequence, key: Any) -> int:
    # add the object element to the end of the list
    # and see list in the order
    # this can save the condition check of 
    # whether the current index is in the length of the list

    a = copy.deepcopy(seq)
    a.append(key)
    
    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('element number : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    ky = int(input('What number do you want to search : '))

    idx = sentinel_search(x, ky)

    if idx == -1:
        print('your value does not exist in the list.')
    else:
        print(f'your value exists in x[{idx}]')
