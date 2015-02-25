from assignment02.geometry import *
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid, Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import PointStamped
from math import sin, cos, degrees

class MapMaker:
    def __init__(self, origin_x, origin_y, resolution, size_x, size_y, transformer):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.resolution = resolution
        self.size_x = size_x
        self.size_y = size_y
        self.transformer = transformer
        
        self.grid = OccupancyGrid()
        self.grid.header.frame_id = 'odom'
        self.grid.info.resolution = resolution
        self.grid.info.width = size_x
        self.grid.info.height = size_y
        self.grid.info.origin.position.x = origin_x
        self.grid.info.origin.position.y = origin_y
        self.grid.info.origin.orientation.w = 1.0
        self.grid.data = [-1] * (size_x * size_y)

        # Insert additional code here if needed

    def to_grid(self, x, y):
        return to_grid(x, y, self.origin_x, self.origin_y, self.size_x, self.size_y, self.resolution)    

    def process_odom(self, msg):
        # Insert your code here
        None

    def process_scan(self, msg):
        # Insert your code here            
        None        
