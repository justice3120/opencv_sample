# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

gray = None

def onTrackbarSlide(pos):
    global gray
    block_size = int(cv2.getTrackbarPos('Block Size', 'Original') * 2 + 3)
    c = cv2.getTrackbarPos('Const', 'Original') / 10
    dst = cv2.adaptiveThreshold(np.array(gray), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)
    cv2.imshow('ADAPTIVE_THRESH_MEAN_C', dst)
    dst = cv2.adaptiveThreshold(np.array(gray), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, c)
    cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C', dst)

def main(args):
    global gray
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

    cv2.namedWindow('Original')
    cv2.namedWindow('ADAPTIVE_THRESH_MEAN_C')
    cv2.namedWindow('ADAPTIVE_THRESH_GAUSSIAN_C')

    cv2.createTrackbar('Block Size', 'Original', 0, 10, onTrackbarSlide)
    cv2.createTrackbar('Const', 'Original', 50, 100, onTrackbarSlide)

    cv2.imshow('Original', gray)

    onTrackbarSlide(100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
