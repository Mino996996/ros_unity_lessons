#!/usr/bin/env python
# coding: UTF-8
import rospy
from std_msgs.msg import String


def on_subscribe(msg: String):
    rospy.loginfo("Subscribe : " + msg.data)


def main():
    rospy.init_node("my_subscriber_node")
    rospy.Subscriber("my_topic", String, on_subscribe)
    rospy.spin()


if __name__ == "__main__":
    main()
