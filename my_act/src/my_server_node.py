#! /usr/bin/env python
# coding: UTF-8
import actionlib
import rospy

# MyActionFeedback,MyActionAction,MyActionResultをインポートする
from my_act.msg import *


def main():
    rospy.init_node("my_server_node")

    def on_request(goal):
        r = rospy.Rate(2)
        for i in range(10):
            feedback = MyActionFeedback(i * 10)
            server.publish_feedback(feedback)
            r.sleep()

        result = MyActionResult(goal.a + goal.b)
        server.set_succeeded(result)

    server = actionlib.SimpleActionServer("my_action", MyActionAction, on_request)

    rospy.spin()


if __name__ == "__main__":
    main()
