'''
Module for image processing functions.
'''

import numpy as np  # only used to create the test image
import cv2

# crop an image
def crop(image, x, y, width, height):
    # TODO add some error checking
    return image[y:y+height, x:x+width]


# rotate an image 90 CW
def rotate_CW(image):
    return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)


# rotate an image 90 CCW
def rotate_CCW(image):
    return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)


# rotate an image 180
def rotate_180(image):
    return cv2.rotate(image, cv2.ROTATE_180)


# flip an image vertically
def flip_vertical(image):
    return cv2.flip(image, 0)


# flip an image horizontally
def flip_horizontal(image):
    return cv2.flip(image, 1)


# debugging main function
def main():
	# add some debugging...


if __name__ == main():
    main()
