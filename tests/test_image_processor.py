'''
TEST THE IMAGE PROCESSOR
'''

import numpy as np

from imagemonk import image_processor as IP

# Test that the image processor functions are working correctly
def test_image_processor():

    # test image used to run the functions
    test_image = np.array([[255,0,255],
                            [0,255,0],
                            [255,0,0]])


    assert IP.crop(test_image,0,0,2,2).shape == (2,2)

    assert IP.crop(test_image,1,1,3,3).shape == (2,2)

    assert (IP.rotate_CW(test_image) == np.array([[255,0,255],
                                                [0,255,0],
                                                [0,0,255]])).all()

    assert (IP.rotate_CCW(test_image) == np.array([[255,0,0],
                                                [0,255,0],
                                                [255,0,255]])).all()

    assert (IP.rotate_180(test_image) == np.array([[0,0,255],
                                                [0,255,0],
                                                [255,0,255]])).all()

    assert (IP.flip_horizontal(test_image) == np.array([[255,0,255],
                                                        [0,255,0],
                                                        [0,0,255]])).all()

    assert (IP.flip_vertical(test_image) == np.array([[255,0,0],
                                                    [0,255,0],
                                                    [255,0,255]])).all()