a, b = input().split()
a = int(a)
b = int(b)


def my(a, b):
    c = 1
    for i in range(b):
        c *= a
    return c


def power(a, b):
    if b == 1: return a
    if b == 0: return 1
    if b != 1: return a * power(a, b - 1)


print(my(a, b))
print(power(a, b))
