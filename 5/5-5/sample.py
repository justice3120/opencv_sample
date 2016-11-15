# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def main(args):
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    dsize = (int(w / 4), int(h / 4))

    cv2.namedWindow('INTER_NEAREST')
    cv2.namedWindow('INTER_LINEAR')
    cv2.namedWindow('INTER_AREA')
    cv2.namedWindow('INTER_CUBIC')
    cv2.namedWindow('INTER_LANCZOS4')

    inter_nearest = cv2.resize(img, dsize, None, 0, 0, cv2.INTER_NEAREST)
    cv2.imshow('INTER_NEAREST', inter_nearest)

    inter_linear = cv2.resize(img, dsize, None, 0, 0, cv2.INTER_LINEAR)
    cv2.imshow('INTER_LINEAR', inter_linear)

    inter_area = cv2.resize(img, dsize, None, 0, 0, cv2.INTER_AREA)
    cv2.imshow('INTER_AREA', inter_area)

    inter_cubic = cv2.resize(img, dsize, None, 0, 0, cv2.INTER_CUBIC)
    cv2.imshow('INTER_CUBIC', inter_cubic)

    inter_lanczos4 = cv2.resize(img, dsize, None, 0, 0, cv2.INTER_LANCZOS4)
    cv2.imshow('INTER_LANCZOS4', inter_lanczos4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
