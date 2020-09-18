'''
TEST THE IMAGE PROCESSOR
'''

import numpy as np

from imagemonk import image_processor as IP

def test_image_processor():

    test_image = np.array([[255,0,255],
                            [0,255,0],
                            [255,0,0]])

    assert IP.flip_horizontal(test_image) == 



