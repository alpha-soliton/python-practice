def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('input the base value : '))
    print(f'The factorial of the {n} is {factorial(n)}.')


