# -*- coding: utf-8 -*-

import sys
import time
import numpy as np
import cv2

def main(args):
    if len(args) != 3:
        return -1
    original_resilution = (2560, 1440)
    template_img = cv2.imread(args[1])
    img = cv2.imread(args[2])
    template_img = cv2.resize(template_img, (int(template_img.shape[0] * img.shape[0] / original_resilution[0]), int(template_img.shape[1] * img.shape[1] / original_resilution[1])))

    cv2.namedWindow('Element Image')
    cv2.namedWindow('TM_SQDIFF')
    cv2.namedWindow('TM_CCORR')
    cv2.namedWindow('TM_CCOEFF')
    cv2.imshow('Element Image', template_img)

    tm_sqdiff = cv2.matchTemplate(img, template_img, cv2.TM_SQDIFF_NORMED)
    f = np.vectorize(lambda x: int((1.0 - x) * 255) )
    tm_sqdiff = f(tm_sqdiff).astype('uint8')
    cv2.imshow('TM_SQDIFF', tm_sqdiff)

    tm_ccorr = cv2.matchTemplate(img, template_img, cv2.TM_CCORR_NORMED)
    f = np.vectorize(lambda x: int(x * 255))
    tm_ccorr = f(tm_ccorr).astype('uint8')
    cv2.imshow('TM_CCORR', tm_ccorr)

    tm_ccoeff = cv2.matchTemplate(img, template_img, cv2.TM_CCOEFF_NORMED)
    f = np.vectorize(lambda x: int(x * 255))
    tm_ccoeff = f(tm_ccoeff).astype('uint8')
    cv2.imshow('TM_CCOEFF', tm_ccoeff)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
