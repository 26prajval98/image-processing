import numpy as np
import cv2
from math import floor
from sys import argv


def blurn(n, img):
    arr = np.shape(img)
    y = arr[0]
    x = arr[1]

    new = np.zeros((y, x), dtype=np.intp)
    start = floor(n/2)
    start = int(start)
    end = n - start

    for j in range(start, x - start):
        for i in range(start, y - start):
            z = img[i - start:i + end, j - start:j + end]
            total = np.sum(np.sum(z))
            new[i, j] = total / (n**2)

    new = np.uint8(new)

    return new


def main(n=3):
    img = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)
    new = blurn(n, img)
    cv2.imshow('Image', new)
    cv2.imshow('Original', img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main(eval(argv[1]))
