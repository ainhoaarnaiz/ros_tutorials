# ROS Tutorials
This is the repository which is going to be used by the student (me!) during the Subject Software II, Introduction to ROS. 

## Assignment 1
Follow the tutorials at [ROS tutorials](https://wiki.ros.org/ROS/Tutorials) from the ROS Wiki, which include:

- **Tutorial 2**: Navigating the ROS Filesystem
- **Tutorial 3**: Creating a ROS package
- **Tutorial 4**: Building a ROS package
- **Tutorial 5**: Understanding ROS Nodes
- **Tutorial 6**: Understanding ROS Topics
- **Tutorial 7**: Understanding ROS Services and Parameters
- **Tutorial 8**: Using rqt_console and roslaunch
- **Tutorial 9**: Using rosed to edit files in ROS
- **Tutorial 10**: Creating a ROS msg and srv
- **Tutorial 11**: Writing a simple Publisher and Subscriber (C++)
- **Tutorial 12**: Writing a simple Publisher and Subscriber (Python)
- **Tutorial 13**: Examining Simple Publisher and Subscriber
- **Tutorial 14**: Writing a Simple Service and Client (C++)
- **Tutorial 15**: Writing a Simple Service and Client (Python)
- **Tutorial 16**: Examining Simple Service and Client
- **Tutorial 17**: Recording and playing back data
- **Tutorial 18**: Recording messages from a bag file

**Result**

```
├── beginner_tutorials
│   ├── bagfiles
│   │   ├── 2024-01-10-02-43-09.bag
│   │   ├── subset.bag
│   │   └── recorded_pose.yaml
│   ├── include
│   ├── launch
│   │   └── turtlemimic.launch
│   ├── msg
│   │   └── Person.msg
│   ├── scripts
│   │   ├── add_two_ints_client.py
│   │   ├── add_two_ints_server.py
│   │   ├── listener.py
│   │   └── talker.py
│   ├── src
│   │   ├── add_two_ints_client.cpp
│   │   ├── add_two_ints_server.cpp
│   │   ├── listener.cpp
│   │   └── talker.cpp
│   ├── srv
│   │   └── AddTwoInts.srv
│   ├── CMakeLists.txt
│   └── package.xml

```

## Assignment 2
1. **Turtle pose subscriber**: write a node that subscribes to the pose of the turtle and prints the position and orientation of the turtle.
2. **Turtle twist publisher**: write a node that publishes a twist message to the turtle.

**Result**

```
├── rospy_tutorial
│   ├── src
│   │   ├── pose_subscriber.py
│   │   └── twist_publisher.py
│   ├── CMakeLists.txt
│   └── package.xml

```
 ![Circular Movement Turtlesim](/z_media/assignment02.png)

## Assignment 3
Upload a screenshot with the vscode running, terminator and rviz opened after launching the simulation in [MRAC_ur_commander](https://github.com/roboticswithjulia/MRAC_ur_commander).

**Result**

 ![Screenshot](/z_media/assignment03.png)