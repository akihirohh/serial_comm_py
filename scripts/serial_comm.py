#!/usr/bin/env python
import rospy
import re 			#regular expressions
import serial
from geometry_msgs.msg import Pose2D

pub = rospy.Publisher('imu', Pose2D, queue_size=1)
rospy.init_node('imu_node')
rate = rospy.Rate(50) #Hz	
pose = Pose2D()
portname = rospy.get_param("/imu/serial_port","/dev/ttyACM0")
serial_port = serial.Serial(portname,115200)
serial_port.flushInput()

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