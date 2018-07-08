import  numpy as np


def eightxeight(img):
    img = np.array(img)
    arr = np.shape(img)
    x = arr[1]
    y = arr[0]
    blocks =[]

    for j in range(0, y, 8):
        line = []
        for i in range(0, x, 8):
            line.append(img[j: j+8, i: i+8])
        blocks.append(line)

    return blocks


if __name__ == '__main__':
    rep = [1, 2, 3, 4, 5, 6, 7, 8]
    x = []
    for i in range(16):
        x.append(rep)