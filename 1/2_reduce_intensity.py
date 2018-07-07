import numpy as np
import cv2


def main(n=2):
    img = cv2.imread("img.png", cv2.IMREAD_GRAYSCALE)
    img = np.floor(img*(1/2**n))*2**n
    img = np.array(img, dtype='uint8')
    cv2.imshow('img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main(7)
