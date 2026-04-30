#error, try java later


def fin(x):
    if x > 1:
        return fin(x-1) + fin(x-2)
    elif x == 1:
        return 1
    else:
        return 0

print(fin(5))
