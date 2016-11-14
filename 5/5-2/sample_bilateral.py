# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

img = None

def onTrackbarSlide(pos):
    update()

def update():
    global img
    d = int(cv2.getTrackbarPos('Diameter', 'Bilateral'))
    sigmaColor = cv2.getTrackbarPos('sigmaColor', 'Bilateral')
    sigmaSpace = cv2.getTrackbarPos('sigmaSpace', 'Bilateral')
    bilateral = cv2.bilateralFilter(np.array(img), d, sigmaColor, sigmaSpace)
    cv2.imshow('Bilateral', bilateral)
    edges = cv2.Canny(cv2.cvtColor(bilateral, cv2.COLOR_RGB2GRAY), 10, 100)
    cv2.imshow('Canny', edges)

def main(args):
    global img

    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    img = cv2.resize(img, (int(img.shape[1] / 4), int(img.shape[0] / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('Bilateral')
    cv2.namedWindow('Canny')

    cv2.createTrackbar('Diameter', 'Bilateral', 5, 100, onTrackbarSlide)
    cv2.createTrackbar('sigmaColor', 'Bilateral', 0, 100, onTrackbarSlide)
    cv2.createTrackbar('sigmaSpace', 'Bilateral', 0, 100, onTrackbarSlide)

    cv2.imshow('Original', img)

    update()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
