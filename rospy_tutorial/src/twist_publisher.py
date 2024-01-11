#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('move_turtle', anonymous=True)
    velocity_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    twist_msg = Twist()
    twist_msg.linear.x = 0.5
    twist_msg.angular.z = 0.2
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        velocity_pub.publish(twist_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
