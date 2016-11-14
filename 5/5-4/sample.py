# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

img = None

def onMouse(event, x, y, flags, param):
    global img
    if (event != 4):
        return

    point = (x , y)
    origin = np.array(img)
    cv2.circle(origin, point, 6, (0, 0, 255), 3)
    cv2.imshow('Original', origin)

    h, w = img.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    mask[:] = 0
    filled = np.array(img)
    ret, rect = cv2.floodFill(filled, mask, point, (255, 255, 255), (25, 25, 25), (25, 25, 25))
    cv2.imshow('Filled', filled)


def main(args):
    global img
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    img = cv2.resize(img, (int(img.shape[1] / 4), int(img.shape[0] / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('Filled')

    cv2.setMouseCallback('Original', onMouse)

    onMouse(4, 100, 100, 0, None)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
