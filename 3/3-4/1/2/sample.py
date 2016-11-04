# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def cvAdd(src1, src2, mask=None):
    src1 = np.array(src1)
    src = src1[:src2.shape[0], :src2.shape[1], :src2.shape[2]]
    src1[:src2.shape[0], :src2.shape[1], :src2.shape[2]] = src + src2
    return src1

def cvAddS(src, value, mask=None):
    return src + value

def cvAddWeighted(src1, alpha, src2, beta, gamma):
    src1 = np.array(src1)
    src = src1[:src2.shape[0], :src2.shape[1], :src2.shape[2]]
    src1[:src2.shape[0], :src2.shape[1], :src2.shape[2]] = (alpha * src) + (beta * src2) + gamma
    return src1

def main(args):
    img1 = cv2.imread(args[1])
    img2 = cv2.pyrDown(cv2.imread(args[2]))
    cv2.namedWindow('cvAdd')
    cv2.imshow('cvAdd', cvAdd(img1, img2))

    cv2.namedWindow('cvAddS')
    cv2.imshow('cvAddS', cvAddS(img1, 50))

    cv2.namedWindow('cvAddWeighted')
    cv2.imshow('cvAddWeighted', cvAddWeighted(img1, 0.4, img2, 0.6, 0))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return

if __name__ == '__main__':
    args = sys.argv
    main(args)
