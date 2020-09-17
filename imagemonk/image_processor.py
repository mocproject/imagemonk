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
def rotate_CCW(image):
    return cv2.rotate(image, cv2.ROTATE_180)


# flip an image vertically
def flip_vertical(image):
    return cv2.flip(image, 0)


# flip an image horizontally
def flip_horizontal(image):
    return cv2.flip(image, 1)


# debugging main function
def main():
    image = np.zeros((5,5))

    image[0,0] = 255
    image[1,1] = 255
    image[0,2] = 255

    image = cv2.resize(image, None, fx=100, fy=100, interpolation = cv2.INTER_NEAREST)

    cv2.imwrite("test.png", image)
    cv2.imwrite("flip.png", flip_vertical(image))


if __name__ == main():
    main()
