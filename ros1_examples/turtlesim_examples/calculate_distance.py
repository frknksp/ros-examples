#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from math import sqrt


def calculate_distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def pose_callback(msg: Pose):
    global firstx, firsty, total_distance

    if firstx is None and firsty is None:
        firstx = msg.x
        firsty = msg.y

    else:
        distance = calculate_distance(msg.x, msg.y, firstx, firsty)
        total_distance += distance
        firstx = msg.x
        firsty = msg.y

        rospy.loginfo(f"Distance traveled: {total_distance}")
        
if __name__ == '__main__':
    firstx = None
    firsty = None
    total_distance = 0.0

    rospy.init_node("turtle_pose_subs")
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    rospy.loginfo("Node has been started")

    rospy.spin()
