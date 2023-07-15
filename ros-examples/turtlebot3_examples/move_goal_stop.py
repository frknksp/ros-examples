#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import sqrt

def calculate_distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def odom_callback(msg: Odometry):
    global firstx, firsty, total_distance
    move_cmd = Twist()


    if firstx is None and firsty is None:
        firstx = msg.pose.pose.position.x
        firsty = msg.pose.pose.position.y

    else:
        distance = calculate_distance(msg.pose.pose.position.x, msg.pose.pose.position.y, firstx, firsty)
        total_distance += distance
        firstx = msg.pose.pose.position.x
        firsty = msg.pose.pose.position.y    

    rospy.loginfo(f"Distance traveled: {total_distance}")

    if total_distance >= target_distance:
        rospy.loginfo("Target distance reached.")
        move_cmd.linear.x = stop_speed
        cmd_vel_pub.publish(move_cmd)
    else:
        move_cmd.linear.x = linear_speed
        cmd_vel_pub.publish(move_cmd)    

if __name__ == '__main__':
    firstx = None
    firsty = None
    linear_speed = 0.2 
    stop_speed = 0.0


    target_distance = 1.0
    total_distance = 0.0  

    rospy.init_node("turtlebot_movement")

    cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    rospy.Subscriber("/odom", Odometry, odom_callback)
    rospy.loginfo("Turtlebot movement started.")

    rospy.spin()
