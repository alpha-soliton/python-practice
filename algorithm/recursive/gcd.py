def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == '__main__':
    print('I will calculate the greatest common divisor of two integers A, B.')
    x = int(input('integer A : '))
    y = int(input('integer B : '))

    print(f'The greatest common divisor of the A and B is {gcd(x, y)}.')
