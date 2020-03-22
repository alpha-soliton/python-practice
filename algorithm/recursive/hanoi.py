def move(no: int, x: int, y: int) -> None:
    # the index of the axis is [1, 2, 3]
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'move disk no.{no} from {x} axis to {y} axis.')

    if no > 1:
        move(no - 1, 6 - x - y, y)

print('The hanoi tower.')

n = int(input('the number of the disk : '))

move(n, 1, 3)
