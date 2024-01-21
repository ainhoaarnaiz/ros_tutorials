from typing import List

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3 , Twist , PoseStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from nav_msgs.srv import GetPlan, GetPlanRequest, GetPlanResponse

#PUBLISHERS
def load_cube_rviz(x:float, y:float, z:float) -> None:
    marker_pub = rospy.Publisher('visualization_marker', Marker, queue_size=10)
    marker = Marker()
    marker.header.frame_id = "base_link"  # assuming TurtleBot's base frame
    marker.header.stamp = rospy.Time.now()
    marker.ns = "basic_shapes"
    marker.id = 2
    marker.type = Marker.CUBE
    marker.action = Marker.ADD

    marker.pose = Pose(Point(x,y, z), Quaternion(0.0, 0.0, 0.0, 1.0))
    marker.scale = Vector3(0.5, 0.5, 0.5)  # cube dimensions

    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0
    marker.color.a = 1.0
    marker.lifetime = rospy.Duration()
    marker_pub.publish(marker)


def cmd_pub(lin_x:float, lin_y:float, rot_z: float) -> None:
    cmd_vel_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    cmd_vel = Twist()
    cmd_vel.linear.x = lin_x
    cmd_vel.linear.y = lin_y
    cmd_vel_pub.publish(cmd_vel)

def move_base_client(x, y, yaw):
    goal_publisher = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    goal_msg = PoseStamped()
    goal_msg.header.frame_id = "map"
    goal_msg.pose.position.x = x
    goal_msg.pose.position.y = y
    goal_msg.pose.orientation.z = yaw  # in radians
    goal_msg.pose.orientation.w = 1.0
    goal_publisher.publish(goal_msg)
    rospy.loginfo(f"Sent goal to move_base: x={x}, y={y}, yaw={yaw}")
    
    

#SUBSCRIBER
def scan_callback(msg):
    ranges = msg.ranges
    rospy.loginfo(f"Received laser scan data: {ranges}")

def laser_sub():
    rospy.Subscriber('/scan', LaserScan, scan_callback)
    rospy.spin()

def odom_callback(msg):
    position = msg.pose.pose.position
    orientation = msg.pose.pose.orientation
    rospy.loginfo(f"Received odometry data - Position: {position}, Orientation: {orientation}")

def odom_sub():
    rospy.Subscriber('/odom', Odometry, odom_callback)
    rospy.spin()


#SERVICES
def make_plan_service(start_x, start_y, start_th, goal_x, goal_y, goal_th):
    request = GetPlanRequest()
    # Set the start pose
    start_pose = PoseStamped()
    request.start.header.frame_id = "map"
    start_pose.header.frame_id = "map"  # Specify the frame, typically "map" for global coordinates
    start_pose.pose.position.x =  start_x # Set the X coordinate of the starting position
    start_pose.pose.position.y = start_y  # Set the Y coordinate of the starting position
    start_pose.pose.orientation.z = start_th  # Set the quaternion orientation (w component) for the goal pose
    start_pose.pose.orientation.w = 1.0
    request.start= start_pose
    
    # Set the goal pose
    goal_pose = PoseStamped()
    request.goal.header.frame_id = "map"
    goal_pose.header.frame_id = "map"  # Specify the frame, typically "map" for global coordinates
    goal_pose.pose.position.x = goal_x # Set the X coordinate of the goal position
    goal_pose.pose.position.y = goal_y  # Set the Y coordinate of the goal position
    goal_pose.pose.orientation.z = goal_th  # Set the quaternion orientation (w component) for the goal pose
    goal_pose.pose.orientation.w = 1.0
    request.goal = goal_pose
    
    # Set a tolerance value for the plan
    request.tolerance = 0.2
    
    try:
        make_plan = rospy.ServiceProxy('/move_base/make_plan', GetPlan)
        response = make_plan(request)
        rospy.loginfo("Received plan successfully")
        return response.plan    
    except rospy.ServiceException as e:
        rospy.logerr(f"Failed to call make_plan service: {e}")
        return []
    

