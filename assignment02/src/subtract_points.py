#!/usr/bin/python

import sys
from assignment02.kinect_bag import *
from sensor_msgs.point_cloud2 import read_points, create_cloud

TOPIC = '/camera/depth_registered/points'

# Loads the PointCloud2 data
background = read_bag_file(sys.argv[1])[TOPIC]
foreground = read_bag_file(sys.argv[2])[TOPIC]

for x,y,z,color in read_points(background):
    rgb = float_to_rgb(color)


# Example new point cloud with one point 
# x=0,y=0,z=1, color=blue
new_points = [ (0,0,1,rgb_to_float(0,0,255)) ]
combined = create_cloud(background.header, background.fields, new_points)
    
new_bag = rosbag.Bag(sys.argv[3], 'w')

try:
    new_bag.write(TOPIC, t)
finally:
    new_bag.close()
