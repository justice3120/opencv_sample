# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def nothing(pos):
    pass

def doPyrDown(img, factor):
    count = factor
    out = img
    while count:
        out = cv2.pyrDown(out)
        count -= 1
    return out

def main(args):
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        return -1

    success, bgr_frame = capture.read()

    cv2.namedWindow('Exercise')
    cv2.createTrackbar('Position', 'Exercise', 0, 7, nothing)
    while success:
        factor = cv2.getTrackbarPos('Position', 'Exercise') + 1
        prydown_frame = doPyrDown(bgr_frame, factor)
        cv2.imshow('Exercise', prydown_frame)
        c = cv2.waitKey(33)
        if c == 27:
            break
        success, bgr_frame = capture.read()

    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
