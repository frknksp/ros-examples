#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2

def pose_callback(msg):
    # Boş bir geri çağırma fonksiyonu
    pass

def move_turtle():
    rospy.init_node('turtle_path_node', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # Yayın hızı (10 Hz olarak ayarlandı)

    # Önceden belirlenmiş yol
    path = [(2.0, 2.0), (3.0, 3.0), (4.0, 2.0), (2.0, 5.0), (10.0, 10.0)]

    for point in path:
        goal_x, goal_y = point[0], point[1]
        cmd = Twist()

        while True:
            pose_msg = rospy.wait_for_message('/turtle1/pose', Pose)
            current_x = pose_msg.x
            current_y = pose_msg.y
            distance = ((goal_x - current_x) ** 2 + (goal_y - current_y) ** 2) ** 0.5

            if distance < 0.1:
                break

            # Hız hesaplama ve ayarlama
            linear_speed = 1.5 * distance
            angular_speed = 4.0 * (atan2(goal_y - current_y, goal_x - current_x) - pose_msg.theta)

            cmd.linear.x = linear_speed
            cmd.angular.z = angular_speed
            pub.publish(cmd)
            rate.sleep()

    # Son konumu almak için bir süre bekleyin
    rospy.sleep(1)

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
