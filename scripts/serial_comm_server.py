#!/usr/bin/env python
import rospy
import re 			#regular expressions
import serial
from geometry_msgs.msg import Pose2D
from serial_comm_py.srv import *

def handle_device(req):
	global serial_port
	print req.turn
	if req.turn:
		try:
			serial_port = serial.Serial(portname,115200)
			serial_port.flushInput()
			return True
		except:
			return False
	else:
		try:
			serial_port.close()
			return True
		except:
			print 'except else'
			return False

pub = rospy.Publisher('imu', Pose2D, queue_size=1)
rospy.init_node('imu_node')
rate = rospy.Rate(50) #Hz	
pose = Pose2D()
portname = rospy.get_param("/imu_node/serial_port","/dev/ttyACM0")
s = rospy.Service('imuDevice',Device, handle_device)

while not rospy.is_shutdown():
	try:
		serial_port.write('I')
		buf=serial_port.readline()
		m=re.findall(r"\d+\.\d*",buf)
		rospy.loginfo(m)
		pose.theta = float(m[0])
		pub.publish(pose)
		rate.sleep()
	except:
		pass
