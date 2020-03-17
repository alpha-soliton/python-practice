from enum import Enum
from open_hash import OpenHash

Menu = Enum('Menu', ['add', 'delete', 'search', 'dump', 'fin'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = ' ', end = '')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = OpenHash(13)

while True:
    menu = select_menu()

    if menu == Menu.add:
        key = int(input('key : '))
        val = input('value : ')
        if not hash.add(key, val):
            print('failed to add element.')

    elif menu == Menu.delete:
        key = int(input('key : '))
        if not hash.remove(key):
            print('failed to delete value.')

    elif menu == Menu.search:
        key = int(input('key : '))
        t = hash.search(key)
        if t is not None:
            print(f'the value of the element  whose Key is {key} is {t}.')
        else:
            print('there is no matching data.')

    elif menu == Menu.dump:
        hash.dump()

    else:
        break
