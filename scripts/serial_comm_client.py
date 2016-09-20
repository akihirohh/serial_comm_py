#!/usr/bin/env python

import sys
import rospy
from serial_comm_py.srv import *

def handle_imu_client(turn):
    rospy.wait_for_service('imuDevice')
    try:
        handle_imu = rospy.ServiceProxy('imuDevice', Device)
        resp1 = handle_imu(turn)
        return resp1.toReturn
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [turn]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        turn = int(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %i"%(turn)
    print "Response: %i"%(handle_imu_client(turn))