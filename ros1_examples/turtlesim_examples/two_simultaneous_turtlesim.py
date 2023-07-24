#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def control_turtlesim():
    rospy.init_node('turtlesim_control', anonymous=True)
    rate = rospy.Rate(10)  # Döngü hızı (10 Hz)

    # İki ayrı Turtlesim robotu için yayıncıları oluşturun
    turtle1_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    turtle2_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

    while not rospy.is_shutdown():
        # Hareket komutlarını oluşturun
        cmd_vel1 = Twist()
        cmd_vel1.linear.x = 1.0  # Turtle1'e ileri gitmek için 1 birim lineer hız verin
        cmd_vel1.angular.z = 0.5  # Turtle1'e saat yönünde 0.5 birim açısal hız verin

        cmd_vel2 = Twist()
        cmd_vel2.linear.x = 0.5  # Turtle2'ye ileri gitmek için 0.5 birim lineer hız verin
        cmd_vel2.angular.z = -0.5  # Turtle2'ye saat yönünün tersine 0.5 birim açısal hız verin

        # Hareket komutlarını yayınlayın
        turtle1_pub.publish(cmd_vel1)
        turtle2_pub.publish(cmd_vel2)

        rate.sleep()

if __name__ == '__main__':
    try:
        control_turtlesim()
    except rospy.ROSInterruptException:
        pass
