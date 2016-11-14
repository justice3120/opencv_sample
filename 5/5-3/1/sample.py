# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def main(args):
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    img = cv2.resize(img, (int(img.shape[1] / 4), int(img.shape[0] / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('Erode')
    cv2.namedWindow('Dilate')

    cv2.imshow('Original', img)

    erode = cv2.erode(np.array(img), None)
    cv2.imshow('Erode', erode)

    dilate = cv2.dilate(np.array(img), None)
    cv2.imshow('Dilate', dilate)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
