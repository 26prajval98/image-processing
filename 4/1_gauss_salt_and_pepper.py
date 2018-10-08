import numpy as np
import cv2
from random import randrange


def create_sp(img, p):
    sp = np.array(img[:, :])
    shape = np.shape(sp)

    itr = int(shape[0]*shape[1]*p/100)
    for i in range(itr):
        x = randrange(0, shape[0])
        y = randrange(0, shape[1])
        if sp[x, y] > 128:
            sp[x, y] = 0
        else:
            sp[x, y] = 255
    return sp


def create_gaussian(img, p):
    g = np.array(img[:, :])

    shape = np.shape(g)
    g = g + np.random.normal(0, p/100, [shape[0], shape[1]])

    g = np.array(g, dtype=np.uint8)

    return g


class Noise:

    percent = 5

    def __init__(self, img):
        self.img = img
        self.salt_pepper = None
        self.gaussian = None

    def add_salt_pepper(self):
        if self.salt_pepper is None:
            self.salt_pepper = create_sp(self.img, type(self).percent)

    def add_gaussian(self):
        if self.gaussian is None:
            self.gaussian = create_gaussian(self.img, type(self).percent)

    @classmethod
    def set_percent(cls, percent):
        cls.percent = percent
        return


def main():
    o = cv2.imread("image_1.png", cv2.IMREAD_GRAYSCALE)
    img = Noise(o)
    img.add_salt_pepper()
    img.add_gaussian()
    cv2.imshow("Original", img.img)
    cv2.imshow("Salt and Pepper", img.salt_pepper)
    cv2.imshow("Gaussian", img.gaussian)
    cv2.waitKey(0)
    return


if __name__ == '__main__':
    main()
