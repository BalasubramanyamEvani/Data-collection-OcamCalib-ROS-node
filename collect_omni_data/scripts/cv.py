#!/usr/bin/env python
'''
@Author: Balasubramanyam Evani
Manipal University Jaipur

Script to divide the frames collected using collect.py as left and right portions for using OcamCalib Toolbox (MATLAB) by David Scaramuzza

'''

## importing necessary libraries

import cv2
import numpy as np
import os
from glob import glob

## path where images are stored

path = '/home/ebs1/catkin_ws/src/collect_omni_data/Images/'



## loading of images
def load_images(path):
	imageList = os.listdir(path)
	images = []
	for image in imageList:
		img_path = os.path.join(path , image)
		img = cv2.imread(img_path)
		images.append(img)
	return images


## separation of images

def separate(images):
	path_left = '/home/ebs1/catkin_ws/src/collect_omni_data/LeftFishEye/' 		## where left images will be written	
	path_right = '/home/ebs1/catkin_ws/src/collect_omni_data/RightFishEye/'		## where right images will be written	
	left = 1									## count for left images, gets incremented
	right = 1                                                                       ## count for right images, gets incremented
	for img in images:								## for every image
		'''
		Take height and width for croppign the individual images
		'''
		height,width = img.shape[:2]
		start_row , start_col = int(0) , int(0)
		end_row , end_col  = int(height) , int(width * .5)
		cropped_left = img[start_row : end_row , start_col : end_col]

		fileName_1 = path_left + str(left) + ".bmp"                             ## images stored as bmp
		cv2.imwrite(fileName_1 , cropped_left)					## left image

		start_row_right , start_col_right = int(0) , int(width * .5)
		end_row_right , end_col_right = int(height) , int(width)
		cropped_right = img[start_row_right : end_row_right , start_col_right : end_col_right]

		fileName_2 = path_right + str(right) + ".bmp"				## images stored as bmp
		cv2.imwrite(fileName_2 , cropped_right)					## right image

		left += 1
		right += 1


## Main function


if __name__ == '__main__':
	images = load_images(path)							## first load all images and store it in a list
	separate(images)								## then separate
