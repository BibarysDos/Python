x, y, z = input().split()


def election(x, y, z):
    sum = int(x) + int(y) + int(z)
    if sum > 2:
        return 1
    else:
        return 0


print(election(x, y, z))
