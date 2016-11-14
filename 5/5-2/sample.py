# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def main(args):
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    img = cv2.resize(img, (int(img.shape[1] / 4), int(img.shape[0] / 4)))

    ksize = (5, 5)

    cv2.namedWindow('Original')
    cv2.namedWindow('Blur')
    cv2.namedWindow('Median')
    cv2.namedWindow('Gaussian')
    cv2.namedWindow('Bilateral')

    cv2.imshow('Original', img)

    blur = cv2.blur(np.array(img), ksize)
    cv2.imshow('Blur', blur)

    median = cv2.medianBlur(np.array(img), 5)
    cv2.imshow('Median', median)

    gaussian = cv2.GaussianBlur(np.array(img), ksize, 0)
    cv2.imshow('Gaussian', gaussian)

    bilateral = cv2.bilateralFilter(np.array(img), 5, 0, 0)
    cv2.imshow('Bilateral', bilateral)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
