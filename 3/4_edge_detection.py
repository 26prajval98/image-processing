import cv2
import numpy as np


def transform(image, mask):
    transformed = np.array(image[:, :, :])
    dim = np.shape(transformed)
    cols = dim[0]
    rows = dim[1]

    dim_mask = np.shape(mask)[0]
    param = int(dim_mask/2)

    for i in range(param, cols-param):
        for j in range(param, rows-param):
            for k in range(3):
                x = np.multiply(image[i - param: i + dim_mask - param, j - param: j + dim_mask - param, k], mask)
                x = int(np.sum(x))
                transformed[i, j, k] = max(min(x, 255), 0)

    return transformed


def main():
    mask = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ], dtype=np.float32)

    image = cv2.imread("img_3.png", cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    masked = transform(image, mask)

    minimum = np.amin(masked)
    maximum = np.amax(masked)

    masked_normal = np.array(((masked - minimum)/(maximum-minimum))*255, dtype=np.uint8)

    cv2.imshow("mask", masked_normal)
    cv2.imshow("sharp", cv2.subtract(image, masked_normal))
    cv2.imshow("original", image)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
