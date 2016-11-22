# -*- coding: utf-8 -*-

import sys
import uuid
import os
import numpy as np
import cv2

args = sys.argv

capture = cv2.VideoCapture(args[1])
save_dir = '/tmp/opencv'

if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

prev_frame = None
while(capture.isOpened()):
    ret, frame = capture.read()
    if frame == None:
      break
    h, w = frame.shape[:2]
    frame = cv2.resize(frame, (int(w / 4), int(h / 4)))
    if prev_frame == None:
        file_name = str(uuid.uuid4()) + '.jpg'
        cv2.imwrite(os.path.join(save_dir, file_name), frame)
    else:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(cv2.matchTemplate(frame, prev_frame, cv2.TM_CCORR_NORMED))
        if max_val < 0.999:
            file_name = str(uuid.uuid4()) + '.jpg'
            cv2.imwrite(os.path.join(save_dir, file_name), frame)
    prev_frame = frame
