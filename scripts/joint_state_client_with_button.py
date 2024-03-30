#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
# TODO 
# Step 1 : Import joint_state_service and joint_state_serviceResponse
from my_robotics.srv import joint_state_service,joint_state_serviceResponse
from Tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create buttons, link it to clickButton() events
        sendButton = Button(self, text="Send Arm Joint State", command=self.clickSendButton)
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        # place button at (0,0)
        sendButton.place(x=20, y=20)
        exitButton.place(x=70, y=60)


    def clickSendButton(self):
        rospy.init_node('JointStateReceiver')
        my_js=rospy.wait_for_message('/joint_states',JointState)
        if (my_js!=None):
            # Step 2 : Call joint_state_transform_request and pass in the Joint State
            # my_js.position[0...5] are [base,shoulder,elbow,wrist_ver,wrist_rot,gripper]
            print('Current Joint State = [base,shoulder,elbow,wrist_ver,wrist_rot,gripper] = [ %.3f %.3f %.3f %.3f %.3f %.3f]'
                %(my_js.position[0],my_js.position[1],my_js.position[2],my_js.position[3],my_js.position[4],my_js.position[5]))
            joint_state_transform_request(my_js.position[0],
                                        my_js.position[1],
                                        my_js.position[2],
                                        my_js.position[3],
                                        my_js.position[4],
                                        my_js.position[5])
        else:
            print('Invalid Joint State ...')

    def clickExitButton(self):
        exit()

def joint_state_transform_request(base,shoulder,elbow,wrist_ver,wrist_rot,gripper):
    rospy.wait_for_service('joint_state_service')
    js_service=rospy.ServiceProxy('joint_state_service',joint_state_service)
    print(js_service(base,shoulder,elbow,wrist_ver,wrist_rot,gripper))

root = Tk()
app = Window(root)
root.wm_title("Braccio Arm Control")
root.geometry("200x100")
root.mainloop()