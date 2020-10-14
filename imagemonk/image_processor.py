'''
Module for image processing functions.
'''
import cv2

# set the bounds of the image
bounds = {
    "MIN_width": 50,
    "MIN_height": 50,
    "MAX_width": 3000,
    "MAX_height": 3000
}


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


# check that the width is within bounds
def check_width(width):
    if bounds["MIN_width"] > width or width > bounds["MAX_width"]:
        raise ValueError("DIMENSION ERROR: WIDTH: " + str(width))


# check that the height is within bounds
def check_height(height):
    if bounds["MIN_height"] > height or height > bounds["MAX_height"]:
        raise ValueError("DIMENSION ERROR: HEIGHT: " + str(height))

'''
Resize image
The image can either be resized using the input dimensions directly, or using the scaling factors. One or the other must be used. If both are supplied to the function, only the dimensions tuple will be used.
'''
def resize(image, dimensions=None, fx=0, fy=0):

    # check if the parameters are inputted correctly
    if dimensions is None and fx == 0 and fy == 0:
        raise AttributeError("NO PARAMETERS INPUTTED")
    
    # if the dimensions tuple is inputted, do not use the scaling factors
    if dimensions is None:
    	check_width(fx * image.shape[1])
        check_height(fy * image.shape[0])

        return cv2.resize(image, None, fx=fx, fy=fy, interpolation = cv2.INTER_CUBIC)

    # if the dimensions tuple is not inputted, use the scaling factors
    else:
        check_width(dimensions[0])
        check_height(dimensions[1])

        return cv2.resize(image, dimensions, interpolation = cv2.INTER_CUBIC)
        


# convert the image to black and white
def black_white(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# convert the image to bgr
def bgr(image):
	return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

