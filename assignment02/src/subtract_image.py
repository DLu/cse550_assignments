#!/usr/bin/python

import sys
from assignment02.kinect_bag import *
import cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

TOPIC = '/camera/rgb/image_rect_color'

background = read_bag_file(sys.argv[1])[TOPIC]
foreground = read_bag_file(sys.argv[2])[TOPIC]

bdata = map(ord, background.data)
fdata = map(ord, foreground.data)

# Insert your code here

background.data = ''.join(map(chr, bdata))

bridge = CvBridge()
cv_image = bridge.imgmsg_to_cv(background)
cv.SaveImage(sys.argv[3], cv_image)
