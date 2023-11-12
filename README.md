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
