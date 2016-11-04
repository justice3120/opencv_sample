# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def cvAbs(src):
    return np.absolute(src)

def cvAbsDiff(src1, src2):
    src = src1[:src2.shape[0], :src2.shape[1], :src2.shape[2]]
    src1[:src2.shape[0], :src2.shape[1], :src2.shape[2]] = np.absolute(src - src2)
    return src1

def cvAbsDiffS(src, value):
    return np.absolute(src - value)

def main(args):
    img1 = cv2.imread(args[1])
    img2 = cv2.pyrDown(cv2.imread(args[2]))
    cv2.namedWindow('cvAbs')
    cv2.imshow('cvAbs', cvAbs(img1))

    cv2.namedWindow('cvAbsDiff')
    cv2.imshow('cvAbsDiff', cvAbsDiff(np.array(img1), img2))

    cv2.namedWindow('cvAbsDiffS')
    cv2.imshow('cvAbsDiffS', cvAbsDiffS(np.array(img1), 100))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return

if __name__ == '__main__':
    args = sys.argv
    main(args)
