import numpy as np
import cv2
from math import floor
from sys import argv


def blurn(n, img):
    arr = np.shape(img)
    y = arr[0]
    x = arr[1]

    start = floor(n/2)
    start = int(start)
    end = n - start
    
    # for all the pixels , replace the value with the average of the values of the neighbouring pixels
    for j in range(start, x - start):
        for i in range(start, y - start):
            z = img[i - start:i + end, j - start:j + end]
            total = np.sum(np.sum(z))
            img[i, j] = total / (n**2)
    img = np.uint8(img)
    return img


def main(n=3):
    print(n)
    # read the image in grayscale
    img = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)
    new = np.array(img, dtype='int')
    new = blurn(n, new)
    cv2.imshow('Image', new)
    cv2.imshow('Original', img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main(eval(argv[1]))
