# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def example2_4(image):
    cv2.namedWindow('Example4-in')
    cv2.namedWindow('Example4-out')

    cv2.imshow('Example4-in', image)

    out = cv2.cv.CreateImage(
        cv2.cv.GetSize(cv2.cv.fromarray(image)),
        cv2.cv.IPL_DEPTH_8U,
        3
    )

    cv2.cv.Smooth(cv2.cv.fromarray(image), out, cv2.cv.CV_GAUSSIAN, 3, 3)

    cv2.imshow('Example4-out', np.asarray(cv2.cv.GetMat(out)))

    cv2.waitKey(0)
    cv2.destroyWindow('Example4-in')
    cv2.destroyWindow('Example4-out')

def main(args):
    img = cv2.imread(args[1])
    example2_4(img)

if __name__ == '__main__':
    args = sys.argv
    main(args)
