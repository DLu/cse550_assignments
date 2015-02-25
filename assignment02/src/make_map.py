#!/usr/bin/python

from assignment02.map_maker import *
import rosbag
import tf
from assignment02.args_parser import parse_args

bagfile, size, origin, resolution, transform = parse_args()

bag = rosbag.Bag(bagfile)

transformer = tf.TransformerROS()
transformer.setTransform(transform)

m = MapMaker(origin, origin, resolution, size, size, transformer)

for topic, msg, t in bag.read_messages():
    if 'Odometry' in str(type(msg)):
        m.process_odom(msg)
    elif 'LaserScan' in str(type(msg)):
        m.process_scan(msg)

bag.close()

s = ''
for y in range(size):
    for x in range(size):
        i = to_index(x,size-y-1,size)
        v = m.grid.data[i]
        
        if v == 0:
            s += ' '
        elif v<0:
            s += '.'
        else:
            s += '#'
            
    s += '\n'
print s                        
