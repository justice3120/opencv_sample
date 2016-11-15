# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

gray = None

def onTrackbarSlide(pos):
    global gray
    ret, dst = cv2.threshold(np.array(gray), int(pos), 255, cv2.THRESH_BINARY)
    cv2.imshow('THRESH_BINARY', dst)
    ret, dst = cv2.threshold(np.array(gray), int(pos), 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('THRESH_BINARY_INV', dst)
    ret, dst = cv2.threshold(np.array(gray), int(pos), 255, cv2.THRESH_TRUNC)
    cv2.imshow('THRESH_TRUNC', dst)
    ret, dst = cv2.threshold(np.array(gray), int(pos), 255, cv2.THRESH_TOZERO)
    cv2.imshow('THRESH_TOZERO', dst)
    ret, dst = cv2.threshold(np.array(gray), int(pos), 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('THRESH_TOZERO_INV', dst)

def main(args):
    global gray
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

    cv2.namedWindow('Original')
    cv2.namedWindow('THRESH_BINARY')
    cv2.namedWindow('THRESH_BINARY_INV')
    cv2.namedWindow('THRESH_TRUNC')
    cv2.namedWindow('THRESH_TOZERO')
    cv2.namedWindow('THRESH_TOZERO_INV')

    cv2.createTrackbar('Threshold', 'Original', 100, 255, onTrackbarSlide)

    cv2.imshow('Original', gray)

    onTrackbarSlide(100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
