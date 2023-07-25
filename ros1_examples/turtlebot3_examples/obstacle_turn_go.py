#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import math

class TurtlebotController:
    def __init__(self):
        rospy.init_node('turtlebot_controller')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.rate = rospy.Rate(10)
        self.obstacle_detected = False
        self.min_value_left = None
        self.min_value_right = None

    def scan_callback(self, data):
        ranges = data.ranges
        front_ranges = ranges[0:15] + ranges[-15:]  # Ön taraftaki mesafeleri al
        right_range = ranges[260:280]
        left_range = ranges[80:100]
        self.min_value_left = min(left_range)
        self.min_value_right = min(right_range)
        print("Ön: ", min(front_ranges), " Sağ: ", min(right_range), " Sol: ", min(left_range))
        

        # Eğer ön tarafta bir engel varsa
        if min(front_ranges) < 1.0:  # 1 metrelik bir eşik değeri
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

    def turn_left(self):
        self.stop()
        rospy.sleep(1)  # Robot'un durması için bir süre bekleme
        twist = Twist()
        twist.angular.z = 1.57 # 90 derece dönüş 
        self.pub.publish(twist)
        rospy.sleep(0.84)  # Dönüş tamamlanması için bir süre bekleme
     
    def turn_right(self):
        self.stop()
        rospy.sleep(1)  # Robot'un durması için bir süre bekleme
        twist = Twist()
        twist.angular.z = -1.57  # -90 derece dönüş
        self.pub.publish(twist)
        rospy.sleep(0.84)  # Dönüş tamamlanması için bir süre bekleme


    def stop(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.pub.publish(twist)

    def run(self):
        while not rospy.is_shutdown():
            if self.obstacle_detected:
                if self.min_value_left is not None and self.min_value_right is not None:
                    if self.min_value_left == "inf":
                        self.turn_left()
                    elif self.min_value_right == "inf":
                        self.turn_right()    
                    elif self.min_value_left < self.min_value_right:
                        self.turn_right()
                    else:
                        self.turn_left()
            else:
                twist = Twist()
                twist.linear.x = 0.20  # Sabit ileri hız (linear x)
                twist.angular.z = 0.0
                self.pub.publish(twist)

            self.rate.sleep()

if __name__ == '__main__':
    controller = TurtlebotController()
    controller.run()