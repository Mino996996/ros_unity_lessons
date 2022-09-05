#! /usr/bin/env python
# coding: UTF-8
import actionlib
import rospy
from my_act.msg import *


def on_feedback(feedback):
    rospy.loginfo("Feedback : " + str(feedback.rate))


def main():
    rospy.init_node("my_client_node")
    client = actionlib.SimpleActionClient("my_action", MyActionAction)
    client.wait_for_server()

    goal = MyActionGoal()
    goal.a = 1
    goal.b = 2

    client.send_goal(goal, feedback_cb=on_feedback)

    client.wait_for_result()

    result = client.get_result()
    rospy.loginfo("Result : " + str(result.sum))

    rospy.spin()


if __name__ == "__main__":
    main()
