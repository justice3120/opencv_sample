# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

img = None

def onTrackbarSlide(pos):
    global img
    ksize = int(cv2.getTrackbarPos('ksize', 'Original') * 2 + 1)
    dst = cv2.Laplacian(np.array(img), cv2.CV_8U, None, ksize)
    cv2.imshow('Laplacian', dst)

def main(args):
    global img
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('Laplacian')

    cv2.createTrackbar('ksize', 'Original', 0, 10, onTrackbarSlide)

    cv2.imshow('Original', img)

    onTrackbarSlide(100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
