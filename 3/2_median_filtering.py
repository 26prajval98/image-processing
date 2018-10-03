import cv2
import numpy as np


def fil(img, n):
    filtered_img = np.array(img)
    dim = np.shape(img)
    cols = dim[0]
    rows = dim[1]
    param = int(n/2)

    for i in range(param, cols - param):
        for j in range(param, rows - param):
            x = np.array(img[i-param:i+n-param, j-param:j+n-param])
            x = np.sort(x, axis=None)

            if n % 2:
                filtered_img[i, j] = x[param]
            else:
                filtered_img[i, j] = (x[param] + x[param - 1])/2

    return filtered_img


def median_filter(n=3):
    noisy_img = cv2.imread('img_s_p.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow("noisy", noisy_img)
    cv2.imshow("median-filtered", fil(noisy_img, n))
    cv2.waitKey(0)


def main():
    median_filter(3)


if __name__ == '__main__':
    main()
