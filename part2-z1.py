# Вариант 1 - моё решение
def fib1(n):
    fn, f1, f2 = 0, 1, 1
    if n in (1, 2):
        return 1
    for i in range(2, n, 1):
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return fn


# Вариант 2 - изящное решение: кортежи и без условия
def fib(n):
    f1, f2 = 0, 1
    while n:
        n -= 1
        f1, f2 = f2, f1 + f2
    return f1


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
