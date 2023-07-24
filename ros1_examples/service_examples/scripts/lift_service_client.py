#!/usr/bin/env python3

import rospy
from service_node.srv import AsansorServis, AsansorServisRequest


def main():
    rospy.init_node('asansor_client')
    rospy.wait_for_service('asansor_servisi')
    try:
        asansor_servisi = rospy.ServiceProxy('asansor_servisi', AsansorServis)
        rakam = int(input("Asansör talebi için bir rakam girin: "))
        request = AsansorServisRequest(rakam)
        response = asansor_servisi(request)
        rospy.loginfo("Cevap: %s", response.cevap)
    except rospy.ServiceException as e:
        rospy.logerr("Servis çağrısı başarısız: %s", str(e))


if __name__ == '__main__':
    main()
