import numpy as np
from math import cos, sqrt, pi


def pixel(blks, i, j):
    return blks[j, i]


def alpha(i, n):
    return sqrt(1/(2*n)) if i != 0 else sqrt(1/n)


def r(u, v, i, j, n):
    return cos(((2*i + 1)*u*pi)/(2*n))*cos(((2*j + 1)*v*pi)/(2*n))


def transform_to_dct(u, v, blks, n):
    return sum(pixel(blks, i, j) * alpha(u, n) * alpha(v, n) * r(u, v, i, j, n) for i in range(n) for j in range(n))


def dct(blks, n=8):
    finalblock = []
    for block in range(len(blks)):
        n_sized_block = blks[block]
        n_sized_block = n_sized_block[0]
        retimg = []
        for v in range(n):
            row = []
            for u in range(n):
                row.append(transform_to_dct(u, v, n_sized_block, n))
            retimg.append(row)

        finalblock.append(retimg)

    return np.floor(np.array(finalblock))


if __name__ == '__main__':
    rep = [1, 2, 3, 4, 5, 6, 7, 8]
    x = []
    for k in range(16):
        x.append(rep)

    x = np.array(x)
