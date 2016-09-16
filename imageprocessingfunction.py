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

#file 1
#im_phase = skimage.io.imread('data/bsub_100x_phase.tif')

#file2
im_phase = skimage.io.imread('data/bsub_100x_phase.tif')



#histogram to figure out threshold
#
# hist_images, bins_images = skimage.exposure.histogram(im_phase)
# plt.plot(bins_images,hist_images)
# plt.xlabel('pixel value')
# plt.ylabel('count')
# plt.show()

def img_segmentation(im_phase, thresh):
    """function to segment any phase contrast image of bacteria"""

    #display the original image
    plt.imshow(im_phase)
    plt.title ('Original Image')
    plt.show()

    #filter out noise using median filters
    # Make the structuring element
    selem = skimage.morphology.square(3)
    # Perform the median filter
    im_phase_med = skimage.filters.median(im_phase, selem)

    # Show filtered image with the viridis LUT.
    plt.imshow(im_phase_med, cmap=plt.cm.Greys_r)
    plt.colorbar()
    plt.title ('Median Filtered Image')
    plt.show()


    #apply a gaussian blur with a 50 pixel radius
    im_phase_gauss = skimage.filters.gaussian(im_phase, 50.0)

    #subtract the background
    # Convert the median-filtered phase image to a float64
    im_phase_float = skimage.img_as_float(im_phase_med)

    # Subtract our gaussian blurred image from the original.
    im_phase_sub = im_phase_float - im_phase_gauss

    #show images side by side (filtered median vs pic with
    #subtracted background)
    fig, ax = plt.subplots(1, 2, figsize=(9.5, 8))
    ax[0].imshow(im_phase_float, cmap=plt.cm.viridis)
    ax[1].imshow(im_phase_sub, cmap=plt.cm.viridis)
    plt.title ('Image With Uniform Background')
    plt.show()

    #generate threshold image
    im_phase_thresh = im_phase_med < thresh

    #show the result
    plt.imshow(im_phase_thresh)
    plt.title ('Threshold Image')
    plt.show()

    #removing objects that are too small
    im_phase_nosmall = morphology.remove_small_objects(im_phase_thresh, min_size=450)
    #min size was only 100 or 200 for the ecoli files, depends on the file type
    plt.imshow(im_phase_nosmall, cmap=plt.cm.Greys_r)
    plt.title ('Image Without Small Objects')
    plt.show()

    #removing objects on/close to the border
    im_phase_noborder=skimage.segmentation.clear_border(im_phase_nosmall,
                      buffer_size=0.2)

    #show the result
    plt.imshow(im_phase_noborder, cmap=plt.cm.Greys_r)
    plt.title ('Final Image')
    plt.show()

img_segmentation(im_phase, 300)
