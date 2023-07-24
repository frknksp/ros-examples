#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math

# Hedef noktaları tanımlayın
points = [(1.0, 0.0), (0.0, 1.0), (1.0, 2.0), (2.0, 1.0)]
current_target = 0  # Başlangıç hedef noktası

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_angle(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)

def odom_callback(data):
    current_x = data.pose.pose.position.x
    current_y = data.pose.pose.position.y

    # Hedefe ulaşıldığında bir sonraki hedef noktasına geç
    target_x, target_y = points[current_target]
    if get_distance(current_x, current_y, target_x, target_y) < 0.1:
        switch_target()

    # Hedefe doğru yönlendirme
    current_yaw = euler_from_quaternion([data.pose.pose.orientation.x,
                                         data.pose.pose.orientation.y,
                                         data.pose.pose.orientation.z,
                                         data.pose.pose.orientation.w])[2]
    target_yaw = get_angle(current_x, current_y, target_x, target_y)
    angular_speed = 0.5
    angle_tolerance = 0.1

    # Hedefe doğru yönlendirme açısını hesaplayın
    angle_diff = target_yaw - current_yaw
    if angle_diff > math.pi:
        angle_diff -= 2 * math.pi
    elif angle_diff < -math.pi:
        angle_diff += 2 * math.pi

    # Hedefe doğru dönme
    if abs(angle_diff) > angle_tolerance:
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = angular_speed * angle_diff
        cmd_vel_pub.publish(twist)
    else:
        # Hedefe doğru yönlendirme tamamlandı, ileri git
        twist = Twist()
        twist.linear.x = 0.2  # Sabit ileri hız
        twist.angular.z = 0.0
        cmd_vel_pub.publish(twist)

def switch_target():
    global current_target
    current_target = (current_target + 1) % len(points)

def main():
    rospy.init_node('turtlebot_controller')
    rospy.Subscriber('/odom', Odometry, odom_callback)
    global cmd_vel_pub
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)  # Hareket hızı

    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
