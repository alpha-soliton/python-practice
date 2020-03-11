from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['add', 'remove', 'search', 'dump', 'terminate'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        else:
            print('input the number in {0} ~ {len(Menu)}')

hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.add:
        key = int(input('key : '))
        val = input('value : ')
        if not hash.add(key, val):
            print('Failed to add.')

    elif menu == Menu.remove:
        key = int(input('key : '))
        if not hash.remove(key):
            print(f'Failed to remove key {key}')
            
    elif menu == Menu.search:
        key = int(input('key : '))
        t = hash.search(key)
        if t is not None:
            print(f'The value of the bucket that has your key is {t}.')
        else:
            print('There is no data which matches your request.')

    elif menu == Menu.dump:
        hash.dump()

    else:
        break
