# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def onTrackbarSlide(pos):
    global img
    sp = cv2.getTrackbarPos('sp', 'Original')
    sr = sp * 2
    maxLevel = cv2.getTrackbarPos('maxLevel', 'Original')

    dst = cv2.pyrMeanShiftFiltering(img.copy(), sp, sr, None, maxLevel)
    cv2.imshow('MeanShift', dst)

def main(args):
    global img
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('MeanShift')

    cv2.createTrackbar('sp', 'Original', 20, 100, onTrackbarSlide)
    cv2.createTrackbar('maxLevel', 'Original', 2, 10, onTrackbarSlide)

    cv2.imshow('Original', img)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
