# serial_comm_py

ROS node to communicate with Arduino in order to obtain IMU measurements. Arduino sends a string containing yaw, pitch, roll in the format I|yaw|pitch|roll|\n  when requested. Currently, only yaw is published as theta of Pose2D ROS message to topic /imu. 

User needs to specify port used by Arduino through rosparam

e.g. rosparam set /imu/serial_port /dev/ttyACM0
