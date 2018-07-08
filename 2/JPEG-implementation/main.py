from app import dct, eight, qt
import  numpy as np

if __name__ == '__main__':
    rep = [1, 2, 3, 4, 5, 6, 7, 8]
    x = []
    for i in range(16):
        x.append(rep)

    encoded = qt.quantize(np.array(dct.dct(eight.eightxeight(x)), dtype='int'))