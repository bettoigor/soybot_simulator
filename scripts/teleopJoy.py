#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################
#                                           #
# Joypad control node for SoyBot            #
#                                           #
# Author: Adalberto Oliveira                #
# Mastering in robotic - PUC-Rio            #   
# Version: 1.0                              #
# Date: 2-13-2019                           #
#                                           #
#############################################

import rospy
import time
import sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy,Image, CameraInfo





def callback_joy(msg):

    global joyCommand
    global vel
    global steer
    global start
    global change_state
    global auto
    global cmd_vel 
    global max_vel
    global max_steer

    joyCommand = msg
    cmdVel = Twist()

    if msg.buttons[0]:
        vel = 0
        steer = 0

    vel = msg.axes[1] * max_vel
    steer = msg.axes[2] * max_steer

    if msg.buttons[10]:
        start = not start
        print('Started...')

    if msg.buttons[1]:
        vel = 0
        steer = 0
        start = False 
        cmdVel.linear.x = 0  
        cmdVel.angular.z = 0
        cmd_vel.publish(cmdVel)
        print('Stopping!')

    if msg.buttons[5]:
        vel = 0
        steer = 0
        cmdVel.linear.x = 0  
        cmdVel.angular.z = 0
        cmd_vel.publish(cmdVel)
        print('Stopping!')

    if msg.buttons[8]:
        auto = True
        vel = 0
        steer = 0
        cmdVel.linear.x = 0  
        cmdVel.angular.z = 0
        cmd_vel.publish(cmdVel)   
        print('Stopping!')


def send_cmd():
    global vel
    global steer
    global start
    global cmd_vel 
    global state

    cmdVel = Twist()

    cmdVel.linear.x = vel
    cmdVel.angular.z = steer

    if not start:
        vel = 0
        steer = 0
        cmdVel.linear.x = 0  
        cmdVel.angular.z = 0

    cmd_vel.publish(cmdVel)

def run():

    global cmd_vel
    global tfBuffer  
    global cv_image
    global change_state

    rospy.init_node("soybot_joy", anonymous=True)
    
    # Publishers
    cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    
    # Subscribers
    rospy.Subscriber('joy', Joy, callback_joy)  

    rate = rospy.Rate(30) 
    time.sleep(2)

    print('Running...')

    while not rospy.is_shutdown():
        send_cmd()
        rate.sleep()


# Main
# GLOBAL VARIABLES
max_vel = float(sys.argv[1])
max_steer = float(sys.argv[2])
joyCommand = Joy()

vel = 0
steer = 0
start = False
auto = False
state = False

if __name__ == '__main__':
    run()


# End Main
