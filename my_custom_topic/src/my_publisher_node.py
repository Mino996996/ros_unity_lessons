#!/usr/bin/env python
# coding: UTF-8
import rospy
from my_custom_topic.msg import MyMessage


def main():
    rospy.init_node("my_publisher_node")

    pub = rospy.Publisher("my_custom_topic", MyMessage, queue_size=10)
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg = MyMessage()
        msg.x = 10
        msg.y = 20

        pub.publish(msg)

        rospy.loginfo("Publish: " + str(msg.x) + "," + str(msg.y))

        r.sleep()


if __name__ == "__main__":
    main()
