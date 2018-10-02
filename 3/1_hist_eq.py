import cv2
import numpy as np
import matplotlib.pyplot as plt


# Integral
def find_s(r, p):
    total = 0
    for i in range(r):
        total += i*p[i]
    return total


def map_vals(vals, img):
    uimg = np.array(img[:, :])
    arr = np.shape(uimg)
    cols = arr[0]
    rows = arr[1]

    for i in range(rows):
        for j in range(cols):
            uimg[j, i] = vals[uimg[j, i]]

    return np.uint8(uimg)


# Read image and generate histogram
def main():
    img = cv2.imread("img.png", cv2.IMREAD_GRAYSCALE)
    vals = img.flatten()
    old_hist = np.histogram(vals, bins=range(256), density=True)[0]
    new_vals = []

    for i in range(255):
        new_vals.append(find_s(i, old_hist))

#   Normalise new values
    minimum = np.amin(new_vals)
    maximum = np.amax(new_vals)

    if minimum < 0 or minimum > 255:
        new_vals = ((new_vals - minimum)*255)/maximum

    new_img = map_vals(new_vals, img)
    cv2.imshow("old_histogram", img)
    cv2.imshow("updated_histogram", new_img)
    plt.plot(range(255), np.histogram(new_img, range(256))[0])
    # plt.plot(range(255), np.histogram(img, range(256))[0])
    plt.show()
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
