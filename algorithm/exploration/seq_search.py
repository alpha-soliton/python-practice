from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    # sequencial search equivalent element to key from the sequence a
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i+=1
    
if __name__ == '__main__':
    num = int(input('num of element : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    ky = int(input('what number do you want to find ? :'))

    idx = seq_search(x, ky)

    if idx == -1:
        print('There is no elememt that matches your request.')
    else:
        print(f'It is the x[{idx}] element.')
