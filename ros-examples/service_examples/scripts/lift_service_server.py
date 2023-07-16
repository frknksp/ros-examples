#!/usr/bin/env python3

from __future__ import print_function

import rospy
from service_node.srv import AsansorServis, AsansorServisResponse


def asansor_kontrol(rakam):
    if rakam > 5:
        return "Asansör kaldırılamıyor - Servis çalışmıyor."
    else:
        return "Asansör kaldırıldı."

def main():
    rospy.init_node('asansor_node')
    rospy.Service('asansor_servisi', AsansorServis, handle_asansor_servisi)
    rospy.spin()

def handle_asansor_servisi(req):
    rospy.loginfo("Asansör talebi alındı: %d", req.rakam)
    response = AsansorServisResponse()
    response.cevap = asansor_kontrol(req.rakam)
    return response

if __name__ == '__main__':
    main()
