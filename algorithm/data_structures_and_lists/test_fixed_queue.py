from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['enque', 'deque', 'peek', 'search', 'dump', 'terminate'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = ' ', end = '')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'The current number of the data : {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.enque:
        x = int(input('data : '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('The queue is full.')

    elif menu == Menu.deque:
        try:
            x = q.deque()
            print(f'The data dequed from the queue is {x}.')
        except FixedQueue.Empty:
            print('The queue is empty.')

    elif menu == Menu.peek:
        try:
            x = q.peek()
            print(f'The peeked data is {x}.')
        except FixedQueue.Empty:
            print('The queue is empty.')

    elif menu == Menu.search:
        x = int(input('the value : '))
        if x in q:
            print(f'Your queue has {q.count(x)} th {x}. The index is {q.find(x)}.')
        else:
            print('Your queue does not have the value.')

    elif menu == Menu.dump:
        q.dump()

    else:
        break


