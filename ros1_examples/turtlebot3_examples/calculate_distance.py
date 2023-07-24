#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import sqrt

def odom_callback(msg: Odometry):
    global firstx, firsty, total_distance

    if firstx is None and firsty is None:
        firstx = msg.pose.pose.position.x
        firsty = msg.pose.pose.position.y
    else:
        distance = sqrt((msg.pose.pose.position.x - firstx)**2 + (msg.pose.pose.position.y - firsty)**2)
        total_distance += distance
        firstx = msg.pose.pose.position.x
        firsty = msg.pose.pose.position.y

        rospy.loginfo(f"Distance traveled: {total_distance}")

if __name__ == '__main__':
    firstx = None
    firsty = None
    total_distance = 0.0

    rospy.init_node("turtlebot_distance_tracker")
    sub = rospy.Subscriber("/odom", Odometry, callback=odom_callback)

    rospy.loginfo("Node has been started")

    rospy.spin()

