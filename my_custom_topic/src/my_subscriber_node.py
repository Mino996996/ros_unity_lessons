#!/usr/bin/env python
# coding: UTF-8
import rospy
from my_custom_topic.msg import MyMessage


def on_subscribe(msg: MyMessage):
    rospy.loginfo("Subscribe : " + str(msg.x) + ", " + str(msg.y))


def main():
    rospy.init_node("my_subscriber_node")

    rospy.Subscriber("my_custom_topic", MyMessage, on_subscribe)

    rospy.spin()


if __name__ == "__main__":
    main()
