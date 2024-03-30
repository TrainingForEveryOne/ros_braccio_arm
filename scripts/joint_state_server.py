#!/usr/bin/env python
import rospy
import serial
# TODO
# Step 1: Import your joint_state_service and joint_state_serviceResponse
from ros_braccio_arm.srv import joint_state_service,joint_state_serviceResponse

base=chr(90)
shoulder=chr(90)
elbow=chr(90)
wrist_ver=chr(90)
wrist_rot=chr(90)
gripper=chr(90)
#arm=serial.Serial("/dev/ttyACM0",115200,timeout=3)

def joint_state_transform(js):
    if (js!=None):
        base=chr(int(js.base/3.14*180))
        shoulder=chr(int(js.shoulder/3.14*180))
        elbow=chr(int(js.elbow/3.14*180))
        wrist_ver=chr(int(js.wrist_ver/3.14*180))
        wrist_rot=chr(int(js.wrist_rot/3.14*180))
        gripper=chr(int(js.gripper/3.14*180))

        rospy.loginfo('Data received: [base,shoulder,elbow,wrist_ver,wrist_rot,gripper] = [%s %s %s %s %s %s]' 
                    % (base,shoulder,elbow,wrist_ver,wrist_rot,gripper))
        pos=[base,shoulder,elbow,wrist_ver,wrist_rot,gripper]
        rospy.loginfo('Sending Joint State ...')
        #state=arm.write(''.join(pos))
        rospy.sleep(2)
        state='Joint State send sucessful.'
        rospy.loginfo('Joint State send sucessful.')
    else:
        rospy.loginfo('Invalid Joint State ...')

    return joint_state_serviceResponse(state) 

def joint_state_server():
    # TODO
    # Step 2 : Initialize a node 'joint_state_service_node'
    # Step 3 : Start a service 'joint_state_service' with type 'joint_state_service', calling 'joint_state_transform' function
    # Step 4 : Spin the node
    rospy.init_node('joint_state_service_node')
    rospy.Service('joint_state_service',joint_state_service,joint_state_transform)
    rospy.spin()

if __name__=='__main__':
    try:
        joint_state_server()
    except rospy.ROSInterruptException:
        pass
