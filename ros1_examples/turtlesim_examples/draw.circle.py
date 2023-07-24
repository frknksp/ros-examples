#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has been started.")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)


    forward_speed = 2.0  # ileri hareket hızı
    angular_speed = 1.0  # açısal hız
    
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = forward_speed
        msg.angular.z = angular_speed
        pub.publish(msg)  

        rate.sleep()

  