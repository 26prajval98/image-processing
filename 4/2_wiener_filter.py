import numpy as np
import cv2

kernel = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]


def wiener(image, k=None):
    image = np.array(image[:, :])

    g = np.fft.fft2(image)
    h = np.fft.fft2(kernel)
    f = np.fft.ifft2(g/h)
    return f


def main():
    image = cv2.imread("image_2.png", cv2.IMREAD_GRAYSCALE)
    f = wiener(image)
    cv2.imshow("Restored", f)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
