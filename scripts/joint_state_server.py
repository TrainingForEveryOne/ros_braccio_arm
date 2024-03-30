#!/usr/bin/env python
import rospy
import serial
# TODO
# Step 1: Import your joint_state_service and joint_state_serviceResponse
from ros_braccio_arm.srv import joint_state_service,joint_state_serviceResponse

base=0
shoulder=90
elbow=90
wrist_ver=0
wrist_rot=0
gripper=60
#arm=serial.Serial("/dev/ttyACM0",115200,timeout=3)
#arm.write(''.join([chr(base),chr(shoulder),chr(elbow),chr(wrist_ver),chr(wrist_rot),chr(gripper)]))

def joint_state_transform(js):
    if (js!=None):
        base=int(js.base/3.14*180)
        shoulder=int(js.shoulder/3.14*180)
        elbow=int(js.elbow/3.14*180)
        wrist_ver=int(js.wrist_ver/3.14*180)
        wrist_rot=int(js.wrist_rot/3.14*180)
        gripper=int(js.gripper/3.14*180)

        rospy.loginfo('Data received: [base,shoulder,elbow,wrist_ver,wrist_rot,gripper] = [%i %i %i %i %i %i]' 
                    % (base,shoulder,elbow,wrist_ver,wrist_rot,gripper))
        pos=[chr(base),chr(shoulder),chr(elbow),chr(wrist_ver),chr(wrist_rot),chr(gripper)]
        rospy.loginfo('Sending Joint State ...')
        #sucess=arm.write(''.join(pos))
        if (sucess==1):
            #rospy.sleep(2)
            state='Joint State send sucessful.'
            rospy.loginfo('Joint State send sucessful.')
        else:
            rospy.loginfo('Send command fail.')
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
