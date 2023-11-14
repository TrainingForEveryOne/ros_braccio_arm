# Activity 1: Create a New Workspace
```
cd ~
mkdir -p ros_train/src
cd ~/ros_train
catkin_make
cd ~/ros_train
source devel/setup.bash
```
# Activity 2: Create a ROS Package
```
cd ~/catkin_ws/src
catkin_create_pkg my_robotics std_msgs rospy roscpp
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```
# Activity 3: Install Github ROS Package
```
cd ~/ros_train/src
git clone https://github.com/tertiarycourses/beginner_tutorials
cd ~/ros_train
catkin_make
source devel/setup.bash
```
# Activity 4: ROS Node
```
roscore  # terminal 1
rosrun turtlesim turtlesim_node  # terminal 2
rosrun turtlesim turtle_teleop_key  # terminal 3, use arrow keys to move the turtle
rosnode list  # terminal 4
rosnode info /teleop_key
```
# Activity 5: ROS Launch
```
# terminal 1
cd ~/catkin_ws/src
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/catkin_ws && catkin_make
source devel/setup.bash

# terminal 2
roscore

# terminal 3
echo "export TURTLEBOT3_MODEL=burger >> ~/.bashrc"
source ~/.bashrc
roslaunch turtlebot3_fake turtlebot3_fake.launch

# terminal 4
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
# Activity 6: ROS Topic
```
roscore  # terminal 1
rosrun turtlesim turtlesim_node  # terminal 2
rosrun turtlesim turtle_teleop_key  # terminal 3, use arrow keys to move the turtle
rostopic list  # terminal 4
rostopic info /turtle1/cmd_vel
rostopic echo /turtle1/cmd_vel
```
# Activity 7: Monitor Topic with RQt
```
rqt
```
# Activity 8: ROS Service
```
roscore  # terminal 1
rosrun turtlesim turtlesim_node  # terminal 2
rosservice list  # terminal 3
rosservice call /spawn 2 2 180 t2
rosservice call /spawn 8 8 0 t3
```
# Activity 9: ROS Parameters
```
roscore  # terminal 1
rosrun turtlesim turtlesim_node  # terminal 2
rosparam list
rosparam get background_g
rosparam set /background_r 150
rosservice call /clear

# if not working
rosparam set /turtlesim/background_r 150
rosservice call /clear
```
# Activity 10: Record and Play ROS Bag
```
roscore  # terminal 1
rosrun turtlesim turtlesim_node  # terminal 2
rosrun turtlesim turtle_teleop_key  # terminal 3
mkdir ~/bagfiles #running rosbag record # terminal 4
cd ~/bagfiles
rosbag record /turtle1/cmd_vel

# Step 1 - Move the turtle using arrow keys
# Step 2 - go to terminal 4, exit with Ctrl-C
rosbag info <bagfile>
rosbag play <bagfile> 
```
# Activity 11: TF Demo -1
```
sudo apt-get install ros-kinetic-turtle-tf2 ros-kinetic-tf2-tools ros-kinetic-tf # terminal 1
roslaunch turtle_tf2 turtle_tr2_demo.launch 
rviz # terminal 2, observe one turtle tracks the other turtle
```
# Activity 12: TF Demo -2
```
# set the fixed frame to /world
# add the TF plugin to the left panel, observe turtle1 and turtle2 frames, both are children of world frame
# set the view of the world to TopDownOrtho
```
# Activity 13: Visualize URDF in RViz
```
# add visual.urdf to the display.launch file
roslaunch my_robotics display.launch model:='visual.urdf'
```
# Activity 14: Xacro
```
# xacro --inorder robot1.xacro > robot1.urdf
roslaunch my_robotics display.launch model:='robot1.urdf' # move the sliders
```
# Braccio Arm Control 
First, check the required packages already install, if not:
```
sudo apt install -y ros-kinetic-joint-state-publisher-gui
sudo apt install -y ros-kinetic-robot-state-publisher
```
Go to workspace src directory and download the ros_braccio_arm package
```
cd ~/catkin_ws/src
git clone http://github.com/twming/ros_braccio_arm.git
```
After download, go to workspace directory and run catkin_make
```
cd ~/catkin_ws
catkin_make
```
Install the successful make package and source the setup.bash
```
catkin_make install
source ~/catkin_ws/devel/setup.bash
```

Launch the Braccio Arm Control package
```
roslaunch ros_braccio_arm arm_launch.xml
```
Control the arm movement from the GUI interface
