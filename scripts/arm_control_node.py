#!/usr/bin/env python

import rospy
import serial
from std_msgs.msg import String
from sensor_msgs.msg import JointState


base=chr(90)
shoulder=chr(90)
elbow=chr(90)
wrist_ver=chr(90)
wrist_rot=chr(90)
gripper=chr(90)

def callback(data):
    base=chr(int(data.position[0]/3.14*180))
    shoulder=chr(int(data.position[1]/3.14*180))
    elbow=chr(int(data.position[2]/3.14*180))
    wrist_ver=chr(int(data.position[3]/3.14*180))
    wrist_rot=chr(int(data.position[4]/3.14*180))
    gripper=chr(int(data.position[5]/3.14*180))
    pos=[base,shoulder,elbow,wrist_ver,wrist_rot,gripper]
    # -- TODO --  print joint angles
    #arm.write(''.join(pos))
    rate = rospy.Rate(0.3)
    rate.sleep()
    

if __name__ == '__main__':
    try:
        #arm=serial.Serial("/dev/ttyACM0",115200,timeout=3)
        rospy.init_node('ArmControl_Node')
        rospy.Subscriber('/joint_states', JointState, callback,queue_size=1)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
