# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

img = None
gray = None
rgb = None
rgb_gray = None

def onTrackbarSlide(pos):
    global gray, rgb_gray
    ret, dst = cv2.threshold(np.array(gray), int(pos), 255, cv2.THRESH_BINARY)
    cv2.imshow('Result GrayScale', dst)
    ret, dst = cv2.threshold(np.array(rgb_gray), int(pos), 255, cv2.THRESH_BINARY)
    cv2.imshow('Result RGB', dst)

def main(args):
    global img, gray, rgb_gray
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    rgb = cv2.split(img)
    rgb_gray = cv2.max(cv2.max(rgb[2], rgb[1]), rgb[0])
    cv2.namedWindow('Result GrayScale')
    cv2.createTrackbar('Threshold', 'Result GrayScale', 100, 255, onTrackbarSlide)
    cv2.namedWindow('Result RGB')

    onTrackbarSlide(100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
