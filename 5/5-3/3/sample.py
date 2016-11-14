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
    cv2.namedWindow('Open')
    cv2.namedWindow('Close')
    cv2.namedWindow('Gradient')
    cv2.namedWindow('Top Hat')
    cv2.namedWindow('Black Hat')

    cv2.imshow('Original', img)

    img_open = cv2.morphologyEx(np.array(img), cv2.MORPH_OPEN, None)
    cv2.imshow('Open', img_open)

    close = cv2.morphologyEx(np.array(img), cv2.MORPH_CLOSE, None)
    cv2.imshow('Close', close)

    gradient = cv2.morphologyEx(np.array(img), cv2.MORPH_GRADIENT, None)
    cv2.imshow('Gradient', gradient)

    top_hat = cv2.morphologyEx(np.array(img), cv2.MORPH_TOPHAT, None)
    cv2.imshow('Top Hat', top_hat)

    black_hat = cv2.morphologyEx(np.array(img), cv2.MORPH_BLACKHAT, None)
    cv2.imshow('Black Hat', black_hat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
