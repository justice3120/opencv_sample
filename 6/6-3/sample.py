# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

img = None

def onTrackbarSlide(pos):
    global img
    dx = int(cv2.getTrackbarPos('dx', 'Original'))
    dy = int(cv2.getTrackbarPos('dy', 'Original'))
    ksize = int(cv2.getTrackbarPos('ksize', 'Original') * 2 + 1)
    dst = cv2.Sobel(np.array(img), cv2.CV_8U, dx, dy, None, ksize)
    cv2.imshow('Sobel', dst)

def main(args):
    global img
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('Sobel')

    cv2.createTrackbar('dx', 'Original', 1, 10, onTrackbarSlide)
    cv2.createTrackbar('dy', 'Original', 0, 10, onTrackbarSlide)
    cv2.createTrackbar('ksize', 'Original', 0, 3, onTrackbarSlide)

    cv2.imshow('Original', img)

    onTrackbarSlide(100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
