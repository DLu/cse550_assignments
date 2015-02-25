#!/usr/bin/python

import rosbag
import struct

def read_bag_file(filename):
    D = {}
    bag = rosbag.Bag(filename)

    for topic, msg, t in bag.read_messages():
        D[topic] = msg
    return D    

def float_to_rgb(x):
    a = struct.unpack('i', struct.pack('f', x))[0]
    r = (a & 0xff0000) >> 16
    g = (a & 0xff00) >> 8
    b = (a & 0xff)
    return r,g,b

def rgb_to_float(r,g,b):
    x = (r << 16) + (g << 8) + b
    a = struct.unpack('f', struct.pack('i', x))[0]
    return a

