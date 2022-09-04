#!/usr/bin/env python
# coring: UTF-8

import rospy
from my_service.srv import MyService


def main():
    rospy.init_node("my_service_client")
    rospy.wait_for_service("my_service")
    try:
        proxy = rospy.ServiceProxy("my_service", MyService)
        result = proxy(1, 2)
        rospy.loginfo("Result : " + str(result.sum))
    except rospy.ServiceException as e:
        rospy.loginfo("ServiceException : %s" % e)

    rospy.spin()


if __name__ == "__main__":
    main()
