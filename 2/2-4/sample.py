# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

slider_position = 0
capture = None

def onTrackbarSlide(pos):
    capture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, float(pos))

def main(args):
    global capture
    global slider_position
    cv2.namedWindow('Example3', cv2.WINDOW_AUTOSIZE)
    capture = cv2.VideoCapture(args[1])
    frames = int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))

    if frames != 0:
        cv2.createTrackbar('Position', 'Example3', slider_position, frames, onTrackbarSlide)

    while(True):
        success, frame = capture.read()
        if not success:
          break
        cv2.imshow('Example3', frame)
        c = cv2.waitKey(33)
        if c == 27:
            break

    capture.release()
    cv2.destroyWindow('Example3')

if __name__ == '__main__':
    args = sys.argv
    main(args)
