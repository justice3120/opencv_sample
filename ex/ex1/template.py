# -*- coding: utf-8 -*-

import sys
import os
import glob
import uuid
import shutil
import random
import numpy as np
import cv2
import copy

def get_similarity_list(img, files):
    similarity_list = []
    for f in files:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(cv2.matchTemplate(img, cv2.imread(f), cv2.TM_CCOEFF_NORMED))
        similarity_list.append((max_val + 1.0) / 2.0)
    return similarity_list

def divide_class(file_list):
    files = copy.deepcopy(file_list)
    m_index = files.index(random.choice(files))
    master = cv2.imread(files[m_index])
    master_sim_list = get_similarity_list(master, files)
    s_index = master_sim_list.index(min(master_sim_list))
    sub = cv2.imread(files[s_index])
    sub_sim_list = get_similarity_list(sub, files)

    class1_files = [files[m_index]]
    class2_files = [files[s_index]]
    class1_sim_list = [master_sim_list[m_index]]
    class2_sim_list = [sub_sim_list[s_index]]

    if m_index > s_index:
        del files[m_index]
        del master_sim_list[m_index]
        del sub_sim_list[m_index]
        del files[s_index]
        del master_sim_list[s_index]
        del sub_sim_list[s_index]
    else:
        del files[s_index]
        del master_sim_list[s_index]
        del sub_sim_list[s_index]
        del files[m_index]
        del master_sim_list[m_index]
        del sub_sim_list[m_index]

    for i in range(len(files)):
        if master_sim_list[i] >= sub_sim_list[i]:
            class1_files.append(files[i])
            class1_sim_list.append(master_sim_list[i])
        else:
            class2_files.append(files[i])
            class2_sim_list.append(sub_sim_list[i])

    class1_min_sim = min(class1_sim_list)
    class2_min_sim = min(class2_sim_list)

    return [class1_files, class2_files, class1_min_sim, class2_min_sim]

def main(args):
    input_dir = '/tmp/opencv'
    result_dir = '/tmp/opencv/result'

    # 結果格納ディレクトリの削除
    if os.path.isdir(result_dir):
        shutil.rmtree(result_dir)

    files = glob.glob(input_dir + '/*.jpg')
    files = random.sample(files, 100)

    min_sim_list = [0.0]
    class_list = [files]

    for i in range(len(files)):
        min_sim = min(min_sim_list)
        if min_sim >= 0.8:
            break
        index = min_sim_list.index(min_sim)
        del min_sim_list[index]
        tmp_files = class_list.pop(index)
        c1, c2, c1_min, c2_min =  divide_class(tmp_files)
        class_list.append(c1)
        class_list.append(c2)
        min_sim_list.append(c1_min)
        min_sim_list.append(c2_min)

        print min_sim_list

    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)

    for i in range(len(class_list)):
        files = class_list[i]
        class_num = str(i)
        file_num = len(files)
        if not os.path.isdir(os.path.join(result_dir, class_num)):
            os.mkdir(os.path.join(result_dir, class_num))
        master_img = None
        for f in files:
            dst_path = os.path.join(result_dir, class_num, os.path.basename(f))
            shutil.copyfile(f, dst_path)
            if master_img == None:
                tmp_img = cv2.imread(f).astype(np.float64)
                master_img = tmp_img / file_num
            else:
                tmp_img = cv2.imread(f).astype(np.float64)
                master_img = master_img + (tmp_img / file_num)
        master_path = os.path.join(result_dir, class_num, 'master.jpg')
        cv2.imwrite(master_path, master_img.astype(np.uint8))

if __name__ == '__main__':
    args = sys.argv
    main(args)
