#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def move_to_goal(goal_pose):
    ac = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    rospy.loginfo("Waiting for move_base action server...")
    ac.wait_for_server()
    rospy.loginfo("Connected to move_base server")

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = goal_pose[0]
    goal.target_pose.pose.position.y = goal_pose[1]
    goal.target_pose.pose.orientation.z = goal_pose[2]
    goal.target_pose.pose.orientation.w = goal_pose[3]

    rospy.loginfo("Sending goal")
    ac.send_goal(goal)

    ac.wait_for_result(rospy.Duration(60))

    if ac.get_state() == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("Goal achieved!")
        return True
    else:
        rospy.loginfo("Failed to achieve goal")
        return False

if __name__ == '__main__':
    try:
        rospy.init_node('turtlebot_mover', anonymous=True)

        goal_poses = [
            [1.0, 0.0, 0.0, 1.0],
            [2.0, 1.0, 0.0, 1.0],
            [0.0, 2.0, 0.0, 1.0]
        ]

        for goal_pose in goal_poses:
            result = move_to_goal(goal_pose)

            if not result:
                rospy.loginfo("Exiting due to goal failure")
                break

    except rospy.ROSInterruptException:
        rospy.loginfo("Interrupted")
