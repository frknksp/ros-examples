#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node("turtlebot_movement")

    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)  

    distance_to_move = 2.0
    linear_speed = 0.2 
    duration = distance_to_move / linear_speed

    move_cmd = Twist()
    move_cmd.linear.x = linear_speed

    start_time = rospy.Time.now().to_sec()

    while not rospy.is_shutdown():
        current_time = rospy.Time.now().to_sec()
        elapsed_time = current_time - start_time
        rospy.loginfo(f"Elapsed time: {elapsed_time:.2f}")

        if elapsed_time < duration:
            pub.publish(move_cmd)
        else:
            break

    move_cmd.linear.x = 0.0
    pub.publish(move_cmd)

    rospy.loginfo("turtlebot stopped")
