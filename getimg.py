#! /usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

# Instantiate CvBridge
bridge = CvBridge()

def image_callback(msg):
	print("Received an image!")
	cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
	#cv2_img = bridge.imgmsg_to_cv2(msg, "32FC1")
	print(cv2_img.shape)
	#原图像高*宽(1080, 1920), -->  (270, 480)
	cv2_img = cv2.resize(cv2_img, (480, 270))
	#cv2.imwrite('camera_image.jpeg', cv2_img)
	cv2.imshow("listener",cv2_img)
	cv2.waitKey(300)

def main():
    	rospy.init_node('image_listener')
	#RGB图像
    	image_topic = "/kinect2/hd/image_color"
	#深度图像
	#image_topic = "/kinect2/hd/image_depth_rect"
    	rospy.Subscriber(image_topic, Image, image_callback)
    	rospy.spin()

if __name__ == '__main__':
   	 main()
