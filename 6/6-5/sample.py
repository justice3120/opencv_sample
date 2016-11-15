# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

gray = None

def onTrackbarSlide(pos):
    global gray
    low_tresh = cv2.getTrackbarPos('Tresh', 'Original')
    aperture_size = int(cv2.getTrackbarPos('apertureSize', 'Original') * 2 + 3)
    dst = cv2.Canny(np.array(gray), low_tresh, low_tresh * 2, None, aperture_size)
    cv2.imshow('Tresh 2:1', dst)
    dst = cv2.Canny(np.array(gray), low_tresh, low_tresh * 3, None, aperture_size)
    cv2.imshow('Tresh 3:1', dst)

def main(args):
    global gray
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

    cv2.namedWindow('Original')
    cv2.namedWindow('Tresh 2:1')
    cv2.namedWindow('Tresh 3:1')

    cv2.createTrackbar('Tresh', 'Original', 0, 100, onTrackbarSlide)
    cv2.createTrackbar('apertureSize', 'Original', 0, 2, onTrackbarSlide)

    cv2.imshow('Original', gray)

    onTrackbarSlide(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
