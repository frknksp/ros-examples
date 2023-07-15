#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose

def callback(msg):
    # Robot's position
    robot_pos = msg.pose.pose.position

    # Engellerin konumları
    engel1_pos = Pose()
    engel1_pos.position.x = 5
    engel1_pos.position.y = 5
    engel1_pos.position.z = 0

    engel2_pos = Pose()
    engel2_pos.position.x = 5
    engel2_pos.position.y = 8
    engel2_pos.position.z = 0

    # Engellerin robota olan uzaklıkları
    engel1_distance = ((engel1_pos.position.x - robot_pos.x)**2 + (engel1_pos.position.y - robot_pos.y)**2 + (engel1_pos.position.z - robot_pos.z)**2)**0.5
    engel2_distance = ((engel2_pos.position.x - robot_pos.x)**2 + (engel2_pos.position.y - robot_pos.y)**2 + (engel2_pos.position.z - robot_pos.z)**2)**0.5

    # En yakın engelin konumu
    if engel1_distance < engel2_distance:
        en_yakin_engel = engel1_pos.position
    else:
        en_yakin_engel = engel2_pos.position

    
    rospy.loginfo("Robota en yakın engel: %s", en_yakin_engel)

if __name__ == "__main__":
    rospy.init_node('engel_hesaplama_node')
    rospy.Subscriber('/odom', Odometry, callback)
    rospy.spin()
