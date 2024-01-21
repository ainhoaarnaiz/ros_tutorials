#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class TurtlebotApprox:
    def __init__(self):
        rospy.init_node('turtlebot_approx', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.target_distance = 0.30
        self.linear_speed = 0.2
        self.angular_speed = 0.0

    def scan_callback(self, scan_data):
        front_distance = scan_data.ranges[len(scan_data.ranges)//2]
        if front_distance > self.target_distance:
            self.linear_speed = 0.2
            self.angular_speed = 0.0
        else:
            self.linear_speed = 0.0
            self.angular_speed = 0.0

    def move_robot(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            twist_cmd = Twist()
            twist_cmd.linear.x = self.linear_speed
            twist_cmd.angular.z = self.angular_speed
            self.cmd_vel_pub.publish(twist_cmd)
            rate.sleep()

if __name__ == '__main__':
    try:
        turtlebot_approx = TurtlebotApprox()
        turtlebot_approx.move_robot()
    except rospy.ROSInterruptException:
        rospy.loginfo("Interrupted")
