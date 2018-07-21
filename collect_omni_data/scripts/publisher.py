#!/usr/bin/env python
'''

@Author:Balasubramanyam Evani
Manipal University Jaipur

ROS node, publishes the result after separation of images from Rico Theta S as Image msg in ROS.

'''
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

class Converter(object):
	def __init__(self):
		self.out_left = rospy.Publisher('omni_Left_Rico',Image, queue_size = 10)
		self.out_right = rospy.Publisher('omni_Right_Rico',Image , queue_size = 10)
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber('/omni_cam/image_raw',Image,self.callback)
	def callback(self,data):
		cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		right , left = self.separate(cv_image)
		try:
			self.out_left.publish(self.bridge.cv2_to_imgmsg(left, "bgr8"))
			self.out_right.publish(self.bridge.cv2_to_imgmsg(right,"bgr8"))
		except CvBridgeError as e:
			print e

	def separate(self,img):

        	height,width = img.shape[:2]
        	start_row , start_col = int(0) , int(0)
        	end_row , end_col  = int(height) , int(width * .5)
        	cropped_left = img[start_row : end_row , start_col : end_col]

        	start_row_right , start_col_right = int(0) , int(width * .5)
        	end_row_right , end_col_right = int(height) , int(width)
        	cropped_right = img[start_row_right : end_row_right , start_col_right : end_col_right]
        	return cropped_right,cropped_left

if __name__ == '__main__':
	rospy.init_node('Rico_Theta_S' , anonymous = True)
	converter = Converter()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Exiting ..")

