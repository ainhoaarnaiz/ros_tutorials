#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def callback(data):
    x = data.x
    y = data.y
    theta = data.theta

    print("Turtle Pose:")
    print("Position: ({}, {})".format(x, y))
    print("Orientation: {}".format(theta))

def turtle_pose_listener():
    rospy.init_node('turtle_pose_listener', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        turtle_pose_listener()
    except rospy.ROSInterruptException:
        pass
