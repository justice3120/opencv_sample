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

    start = time.time()
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(cv2.matchTemplate(img, template_img, cv2.TM_SQDIFF_NORMED))
    elapsed_time = time.time() - start
    print ("elapsed_time for TM_SQDIFF:{0}".format(elapsed_time)) + "[sec]"
    print min_val, max_val
    tm_sqdiff = np.array(img)
    cv2.rectangle(tm_sqdiff, min_loc, (min_loc[0] + template_img.shape[0], min_loc[1] + template_img.shape[1]), (0, 0, 255), 3)
    cv2.imshow('TM_SQDIFF', tm_sqdiff)

    start = time.time()
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(cv2.matchTemplate(img, template_img, cv2.TM_CCORR_NORMED))
    elapsed_time = time.time() - start
    print ("elapsed_time for TM_CCORR:{0}".format(elapsed_time)) + "[sec]"
    print min_val, max_val
    tm_ccorr = np.array(img)
    cv2.rectangle(tm_ccorr, max_loc, (max_loc[0] + template_img.shape[0], max_loc[1] + template_img.shape[1]), (0, 0, 255), 3)
    cv2.imshow('TM_CCORR', tm_ccorr)

    start = time.time()
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(cv2.matchTemplate(img, template_img, cv2.TM_CCOEFF_NORMED))
    elapsed_time = time.time() - start
    print ("elapsed_time for TM_CCOEFF:{0}".format(elapsed_time)) + "[sec]"
    print min_val, max_val
    tm_ccoeff = np.array(img)
    cv2.rectangle(tm_ccoeff, max_loc, (max_loc[0] + template_img.shape[0], max_loc[1] + template_img.shape[1]), (0, 0, 255), 3)
    cv2.imshow('TM_CCOEFF', tm_ccoeff)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
