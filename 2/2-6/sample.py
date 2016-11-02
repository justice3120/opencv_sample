# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def doPyrDown(img):
    assert (img.width % 2) == 0 and (img.height % 2) == 0

    out = cv2.cv.CreateImage(
        (img.width / 2, img.height / 2),
        img.depth,
        img.nChannels
    )

    cv2.cv.PyrDown(img, out)
    return out

def doCanny(img, lowThresh, highThresh, aperture):
    if img.nChannels != 1:
        return None

    out = cv2.cv.CreateImage(
        cv2.cv.GetSize(img),
        img.depth,
        1
    )
    cv2.cv.Canny(img, out, lowThresh, highThresh, aperture)
    return out

def main(args):
    img = cv2.cv.LoadImage(args[1], cv2.cv.CV_LOAD_IMAGE_GRAYSCALE)
    cv2.namedWindow('Example', cv2.WINDOW_AUTOSIZE)

    out = doPyrDown(img)
    out = doPyrDown(out)
    out = doCanny(out, 10, 100, 3)
    cv2.cv.ShowImage('Example', out)

    cv2.waitKey(0)
    cv2.destroyWindow('Example')

if __name__ == '__main__':
    args = sys.argv
    main(args)
