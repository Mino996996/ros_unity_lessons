#!/usr/bin/env python
# coding: UTF-8

import rospy
from my_service.srv import MyService, MyServiceResponse


def on_request(req):
    srv = MyServiceResponse()
    srv.sum = req.a + req.b
    return srv


def main():
    rospy.init_node("my_server_node")
    rospy.Service("my_service", MyService, on_request)
    rospy.spin()


if __name__ == "__main__":
    main()
