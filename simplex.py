## module to compute simplex algorithm

"""
simplex method
"""

def     simplex(data, product):
    while count_neg(data) > 0:
        print(data)
        pivot = choose_pivot(data)
        if pivot[0] == -1 or pivot[1] == -1:
            return
        set_pivot(data, pivot[0], pivot[1])
        if pivot[1] in range(len(product)):
            product[pivot[1]] = pivot[0]
        else:
            print("hi")
            product[pivot[1] % len(product)] = pivot[0]
    print(data)

"""
get pivot
"""

def     choose_pivot(data):
    xmax = len(data[0])
    ymax = len(data)
    minimum = float("inf")
    xpiv = -1
    ypiv = -1

    for x in range(xmax):
        if data[ymax - 1][x] < minimum:
            minimum = data[ymax - 1][x]
            xpiv = x

    minimum = float("inf")

    for y in range(ymax - 1):
        if data[y][xpiv] != 0 and data[y][xmax - 1] / data[y][xpiv] > 0 and data[y][xmax - 1] / data[y][xpiv] < minimum:
            minimum = data[y][xmax - 1] / data[y][xpiv]
            ypiv = y

    return (ypiv, xpiv)

"""
set pivot to 1 and adjacent to 0
"""

def     set_pivot(data, ypiv, xpiv):
    xmax = len(data[0])
    ymax = len(data)
    div = data[ypiv][xpiv]

    if div == 0:
        return

    for x in range(xmax):
        data[ypiv][x] /= div

    for y in range(ymax):
        if y != ypiv:
            mult = -data[y][xpiv]
            for x in range(xmax):
                data[y][x] += (mult * data[ypiv][x])

"""
count negative numbers in expression
"""

def     count_neg(data):
    xmax = len(data[0])
    ymax = len(data)
    count = 0

    for x in range(xmax):
        if data[ymax - 1][x] < 0:
            count += 1

    return count
