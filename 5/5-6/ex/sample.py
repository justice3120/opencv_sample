# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def main(args):
    if len(args) != 2:
        return -1
    img = cv2.imread(args[1])
    h, w = img.shape[:2]
    img = cv2.resize(img, (int(w / 4), int(h / 4)))

    cv2.namedWindow('Original')
    cv2.namedWindow('1 Step')
    cv2.namedWindow('2 Step')
    cv2.namedWindow('3 Step')
    cv2.namedWindow('1 Step Diff')
    cv2.namedWindow('2 Step Diff')
    cv2.namedWindow('3 Step Diff')

    cv2.imshow('Original', img)

    step_1 = cv2.pyrUp( cv2.pyrDown(np.array(img)) )
    cv2.imshow('1 Step', step_1)

    step_2 = cv2.pyrUp(cv2.pyrUp( cv2.pyrDown(cv2.pyrDown(np.array(img))) ))
    cv2.imshow('2 Step', step_2)

    step_3 = cv2.pyrUp(cv2.pyrUp(cv2.pyrUp( cv2.pyrDown(cv2.pyrDown(cv2.pyrDown(np.array(img)))) )))
    cv2.imshow('3 Step', step_3)

    step_1_diff = np.absolute(img - step_1)
    cv2.imshow('1 Step Diff', step_1_diff)

    step_2_diff = np.absolute(step_1 - step_2)
    cv2.imshow('2 Step Diff', step_2_diff)

    step_3_diff = np.absolute(step_2 - step_3)
    cv2.imshow('3 Step Diff', step_3_diff)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
