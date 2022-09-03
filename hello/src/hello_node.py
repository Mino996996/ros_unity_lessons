#!/usr/bin/env python
# coding: UTF-8
import rospy


def main():
    # ノードの生成
    rospy.init_node("hello_node")

    # ログの出力
    rospy.loginfo("Hello World!")

    # ノード終了まで待機
    rospy.spin()


if __name__ == "__main__":
    main()
