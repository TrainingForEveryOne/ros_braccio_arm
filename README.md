# Unix Command Tips
```
ls              # list the items in the directory
cd my_folder    # change directory to my_folder
cd ..           # change directory to parent folder
cd ~            # change directory to /home/ros folder
mkdir my_folder # create new my_folder directory
rmdir my_folder # remove my_folder directory
rm file         # remove file
sudo apt-get install package_name # install package_name
```
# Useful package for multi-window terminal (optional)
```
sudo apt install terminator # for multi-window terminal
```
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
rosnode info /teleop_turtle
```
# Activity 5: ROS Launch
```
# terminal 1
cd ~/catkin_ws/src
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
sudo apt install ros-kinetic-turtlebot3 # install the dependency turtlebot3 package
cd ~/catkin_ws && catkin_make
source devel/setup.bash

# terminal 2
roscore

# terminal 3
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
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
roslaunch turtle_tf2 turtle_tf2_demo.launch 
rviz # terminal 2, observe one turtle tracks the other turtle
```
# Activity 12: TF Demo -2
```
# set the fixed frame to /world
# add the TF plugin to the left panel, observe turtle1 and turtle2 frames, both are children of world frame
# set the view of the world to TopDownOrtho
```
# Activity 13: Construct display.launch file
```
# add display.launch file to launch folder
sudo apt install -y ros-kinetic-joint-state-publisher-gui
cd ~/ros_train/src
git clone https://github.com/twming/ros_braccio_arm
cd ~/ros_train
catkin_make

cd ~/ros_train/src/ros_braccio_arm/launch
touch display.launch
gedit display.launch

# create a new file launch in this folder
<launch>
  <arg name="gui" default="true" />
  <param name="robot_description" command="$(find xacro)/xacro $(arg model)" />
  <node if="$(arg gui)" name="joint_state_publisher" pkg="joint_state_publisher_gui" type="joint_state_publisher_gui" />
  <node unless="$(arg gui)" name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher" />
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />
  <node name="rviz" pkg="rviz" type="rviz" args="-d $(find ros_braccio_arm)/rviz/urdf.rviz" required="true" />
</launch>
```
# Activity 14: Xacro and Visualize URDF in RViz
```
cd ~/ros_train/src/ros_braccio_arm/urdf
xacro --inorder robot1.xacro > robot1.urdf

cd ~/ros_train
catkin_make
source devel/setup.bash
roslaunch ros_braccio_arm display.launch model:='/home/ros/ros_train/src/ros_braccio_arm/urdf/robot1.urdf'
# Add -> RobotModel
# move the sliders
```
# (Optional) Braccio Arm Setup 
First, check the required packages already install, if not:
```
sudo apt install -y ros-kinetic-joint-state-publisher-gui
sudo apt install -y ros-kinetic-robot-state-publisher
```
Setup your VM USB port, (Right Click) Setting -> USB -> Arduino (Add). Modify the ttyACM0 and *.py to 755
```
sudo chmod 777 /dev/ttyACM0
sudo chmod 755 /home/ros/ros_train/src/ros_braccio_arm/scripts/*.py
```
Uncomment the arm write (line 25) and serial write (line 32) in the file arm_control_node.py. Launch the Braccio Arm Control package
```
roslaunch ros_braccio_arm arm_launch
```
# (Optional) Braccio Arm Control through JointState Message
Control the arm movement from the GUI interface. Launch the Braccio Arm Joint State write through Topic
```
rosrun ros_braccio_arm arm_control_node.py
```
# (Optional) Braccio Arm Control through JointState Service
Uncomment the arm write (line 14,15,30) in the file joint_state_server.py. Launch the Braccio Arm Joint State write through Service
```
rosrun ros_braccio_arm joint_state_server.py
rosrun ros_braccio_arm joint_state_client_with_button.py
```
