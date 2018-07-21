#!/usr/bin/env python
'''
@Author: Balasubramanyam Evani
Manipal University Jaipur

Script to collect images from Ricoh Theta S 

'''

## import required libraries

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

## Class TakeSnapshot implements methods needed for capturing and saving image

class TakeSnapshot(object):
	def __init__(self): 
		self.camera_topic = rospy.get_param("~camera_topic", '/omni_cam/image_raw') ## topic where image is publishing
		self.image_num = 1 							   ## starting number of image, increments when taking more data
		self.output_dir = '/home/ebs1/catkin_ws/src/collect_omni_data/Images/'     ## directory where to store, change accordingly
		self.bridge = CvBridge()						   ## CvBridge object creation

	def run(self):
		print "Collection Started, Press q to exit"	
		while not rospy.is_shutdown():						   
			str = raw_input()						   ## observes input
			if "q" in str:							   ## if 'q' pressed, the program exits
				break
			try:
				camera_msg = rospy.wait_for_message(self.camera_topic, Image, timeout=0.25)	## else records msg
			except rospy.exceptions.ROSException as err:
                		print "Failed to receive camera message: " + str(err)
                		continue
			self.process_image(camera_msg)					   ## process method called, which converts ros Image msg to cv2 frame
			self.image_num += 1                                                ## increments the image number

	def process_image(self, camera_msg):
		filename = self.output_dir + "/image%03d.bmp" % self.image_num	           ## file_name under which it will be stored
		print filename                                                             ## when saved prints file name
        	try:
            		cv_image = self.bridge.imgmsg_to_cv2(camera_msg, "bgr8")           ## conversion of img msg to cv2 
        	except CvBridgeError as err:
			print str(err)
            		raise err
        	try:
            		cv2.imwrite(filename, cv_image)					   ## writing the image as bmp format
		except Exception as err:
            		print str(err)
            		raise err


if __name__ == '__main__':
	node = "collector"							       	   ## Node name
	rospy.init_node(node)			                                           ## initialize node
	snapshot = TakeSnapshot()						           ## object of class Takesnapshot
	snapshot.run()                                                                     ## starts taking the snapshots
