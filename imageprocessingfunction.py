#Lesson 40 Practice 1-Writing your own segementation function
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

import skimage.io
import skimage.filters
import skimage.measure
import skimage.segmentation
from skimage import morphology

#Load the image
im_phase = skimage.io.imread('data/bsub_100x_phase.tif')

#do histogram to determine threshold pixel value
# Get the histogram data
hist_phase, bins_phase = skimage.exposure.histogram(im_phase)


def img_segmentation(im_phase, thresh):
    """function to segment any phase contrast image of bacteria"""

    #display the original image
    plt.imshow(im_phase)



    #filter out noise using median filters
    # Make the structuring element
    selem = skimage.morphology.square(3)
    # Perform the median filter
    im_phase_med = skimage.filters.median(im_phase, selem)



    # Show filtered image with the viridis LUT.
    plt.imshow(im_phase_med, cmap=plt.cm.Greys_r)
    plt.colorbar()
    plt.show()

    #generate threshold image
    im_phase_thresh = im_phase_med < thresh

    #show the result
    plt.imshow(im_phase_thresh)
    plt.show()

    #removing objects that are too small
    im_phase_nosmall = morphology.remove_small_objects(im_phase_thresh, min_size=100)
    plt.imshow(im_phase_nosmall, cmap=plt.cm.Greys_r)
    plt.show()

    #removing objects on/close to the border
    im_phase_noborder=skimage.segmentation.clear_border(im_phase_nosmall,
                      buffer_size=0.2)

    #show the result
    plt.imshow(im_phase_noborder, cmap=plt.cm.Greys_r)
    plt.show()

img_segmentation(im_phase, 220)
