# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2

def main(args):
    capture = cv2.VideoCapture(args[1])
    if not capture.isOpened():
        return -1

    success, bgr_frame = capture.read()

    fps = capture.get(cv2.cv.CV_CAP_PROP_FPS)
    size = (
        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    )
    writer = cv2.VideoWriter(
        args[2],
        cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'),
        fps,
        size
    )
    logpolar_frame = cv2.cv.CreateImage(
        size,
        cv2.cv.IPL_DEPTH_8U,
        3
    )
    while success:
        bgr_frame = cv2.cv.fromarray(bgr_frame)
        cv2.cv.LogPolar(bgr_frame, logpolar_frame,
            (bgr_frame.width / 2, bgr_frame.height / 2), 40,
            cv2.cv.CV_INTER_LINEAR + cv2.cv.CV_WARP_FILL_OUTLIERS
        )
        writer.write(np.asarray(cv2.cv.GetMat(logpolar_frame)))
        success, bgr_frame = capture.read()

    capture.release()
    return 0

if __name__ == '__main__':
    args = sys.argv
    main(args)
