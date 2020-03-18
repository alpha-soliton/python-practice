from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['push', 'pop', 'peek', 'search', 'dump', 'terminate'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    #type_check = type((*s))
    #print(f'type of *[] : {type_check}')
    while True:
        print(*s, sep = ' ', end= '')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)

while True:
    print(f'current number of the data : {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.push:
        x = int(input('data : '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('the stack if full.')

    elif menu == Menu.pop:
        try:
            x = s.pop()
            print(f'popped data is {x}.')
        except FixedStack.Empty:
            print('the stack is empty.')

    elif menu == Menu.peek:
        try:
            x = s.peek()
            print(f'peeked data is {x}.')
        except FixedStack.Empty:
            print('the stack is empty.')

    elif menu == Menu.search:
        x = int(input('value : '))
        if x in s:
            print(f'The stack has {s.count_value(x)} {x}. The top value is in {s.find(x)}.')
        else:
            print('the stack does not have the value.')

    elif menu == Menu.dump:
        s.dump()


    else:
        break
