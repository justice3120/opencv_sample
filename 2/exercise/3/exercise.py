# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def doPyrDown(img):
    return cv2.pyrDown(img)

def main(args):
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        return -1

    success, bgr_frame = capture.read()

    fps = capture.get(cv2.cv.CV_CAP_PROP_FPS)
    size = (
        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH) / 2),
        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT) / 2)
    )
    writer = cv2.VideoWriter(
        args[1],
        cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'),
        fps,
        size
    )
    prydown_frame = cv2.cv.CreateImage(
        size,
        cv2.cv.IPL_DEPTH_8U,
        3
    )
    while success:
        prydown_frame = doPyrDown(bgr_frame)
        writer.write(prydown_frame)
        success, bgr_frame = capture.read()

    capture.release()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
