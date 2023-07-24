import rospy
from asansor_servisi.srv import AsansorServis, AsansorServisResponse


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
