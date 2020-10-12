####
# This file is for reading image and saving results

import os
import cv2


# read files and images
def read_img(path):
    """
    :param path: cwd
    :return: a dictionary with sequence folders (in which are the images)
    """
    sequence_tif = {}
    for root, dirs, _, in os.walk(path):
        dirs.sort()
        for dir in dirs:
            sequence_tif[dir] = []
            for _, _, files in os.walk(os.path.join(path, dir)):
                files.sort()
                for file in files:
                    new_dir_path = os.path.join(path, dir)
                    temp_img = cv2.imread(os.path.join(new_dir_path, file))
                    sequence_tif[dir].append(temp_img)
    return sequence_tif


def write_img(img, fdname, index):
    """
    :param img:
    :param fdname:  folder name
    :param seq:  index of image
    :return:
    """
    if type(fdname) != str or type(index) != int:
        print("wrong input")
        raise SystemExit
    fdname = ''.join([i for i in fdname.split()])
    cwd = os.getcwd()
    folder_path = cwd + '\\' + fdname
    if os.path.exists(folder_path):
        pass
    else:
        os.makedirs(folder_path)

    try:
        cv2.imwrite(folder_path + '\\' + '{:0>4d}'.format(index) + '.jpg', img)
    except IOError:
        print("Writing Failure")


# def delete_folder(name):
#     if type(name) != str:
#         raise SystemExit
#     folder_name = '\\' + name
#     cwd = os.getcwd()
#     folder_path = cwd + folder_name
#     print(folder_path)
#     try:
#         if os.path.exists(folder_path):
#             flag = os.removedirs(folder_path)
#             print(f'removed {flag}')
#     except IOError:
#         print("Deletion Failure")
