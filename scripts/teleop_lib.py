import rospy
import time
import sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy,Image, CameraInfo

class Teleop

    def __init__(self):

        self.vel = 0
        self.steer = 0
        self.start = False
        self.change_stata = False
        self.auto = False
        self.cmd_vel = Twist()
        self.__MAX_VEL = 1
        self.__MAX_STEER = 1

    def set_max(self,max_vel = 1,max_steer = 1):

        self.__MAX_VEL = max_vel
        self.__MAX_STEER = max_steer

    def