####
# This file is for preprocessing img
import cv2
import numpy as np
from skimage.morphology import watershed
from skimage.feature import peak_local_max
from scipy import ndimage as ndi
import skimage


def normalize(input_img):
    return ((input_img - input_img.min()) / (input_img.max() - input_img.min()) * 255).astype(np.uint8)


def preprocess_set1(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    re, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    opening = cv2.erode(thresh, kernel2, iterations=3)
    opening = cv2.dilate(opening, kernel2, iterations=3)
    labels = skimage.measure.label(opening, connectivity=2)
    return normalize(img).copy(), labels


def preprocess_set2(img):
    '''
    :param img:
    :return: background, opening
        background:normalized gray image for drawing rectangular
        opening: result
    '''
    # set the kernel size
    kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # top hat operation
    new = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel1)
    illumination_corrected = cv2.convertScaleAbs(gray - new)
    # Fill inner holes
    cleaned = cv2.morphologyEx(illumination_corrected, cv2.MORPH_CLOSE, kernel1)
    # blur
    blur = cv2.GaussianBlur(cleaned, (9, 9), 0)
    # normalize the intensity
    normal = normalize(blur)
    # finding the threshold
    threshold = np.unique(normal)[1]
    # find the binary mask
    mask = np.array(normal > threshold).astype(np.uint8)
    # erosion and dilation
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    opening = cv2.erode(mask, kernel2, iterations=3)
    opening = cv2.dilate(opening, kernel2, iterations=3)

    return normalize(gray).copy(), opening


def preprocess_set3(img):
    '''
    :param img:
    :return: background, opening
        background:normalized gray image for drawing rectangular
        opening: result
    '''
    # set the kernel size
    kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # normalize the intensity
    normal = normalize(gray)
    # top hat operation
    new = cv2.morphologyEx(normal, cv2.MORPH_TOPHAT, kernel1)
    # illumination_corrected = cv2.convertScaleAbs(gray - new)
    # Fill inner holes
    cleaned = cv2.morphologyEx(new, cv2.MORPH_CLOSE, kernel1)
    # blur
    blur = cv2.GaussianBlur(cleaned, (9, 9), 0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    opening = cv2.erode(thresh, kernel2, iterations=3)
    opening = cv2.dilate(opening, kernel2, iterations=3)

    return normalize(gray).copy(), opening


def watershed_algorithm(input):
    """
    using watershed alghorithm to segement the image
    :param opening:
    :return:
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    dt = cv2.distanceTransform(input, cv2.DIST_L2, 3)
    distance = cv2.GaussianBlur(normalize(dt), (5, 5), -1)
    local_max = peak_local_max(0.2 * distance, indices=False, labels=input, footprint=kernel)
    markers = ndi.label(local_max, np.ones((3, 3)))[0]
    ws_labels = watershed(-distance, markers, mask=input)
    return ws_labels
