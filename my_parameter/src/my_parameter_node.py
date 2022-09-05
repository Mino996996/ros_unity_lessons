#! /usr/bin/env python
# coding: UTF-8
import rospy


def main():
    rospy.init_node("my_parameter_node")
    if not rospy.has_param("~my_parameter"):
        # ここの値は設定値
        rospy.set_param("~my_parameter", 0)

    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        # ここの値はデフォルト値
        value = rospy.get_param("~my_parameter", 0)
        rospy.loginfo("my_parameter : " + str(value))
        r.sleep()

    rospy.spin()


if __name__ == "__main__":
    main()
