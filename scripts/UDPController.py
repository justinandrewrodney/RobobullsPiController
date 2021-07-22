#This is a UDP-controller/Server that controls the robot's speeds
#This uses drivers adapted from: https://github.com/biorobaw/pi3_robot_2019

#Import
import socket
import sys

import os
#Imports drivers for servos
driver_folder = "/home/pi/Desktop/UDPController/drivers"
sys.path.append(os.path.abspath(driver_folder))
import MyMotors

driver_folder = "/home/pi/Desktop/UDPController/protos"
sys.path.append(os.path.abspath(driver_folder))
import pirobot2019_pb2

MyMotors.setSpeeds(0,0)


#UDP_IP  =  "127.0.0.1"
UDP_IP = "10.224.250.190"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
try: 
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        #data = str(data)
        velocity = pirobot2019_pb2.VelocityXYZ()
        
        ##msg_type = ord(data[0]) #checks first byte to determine message type
        msg_type = data[0]
        if(msg_type == 0):# msg is speed data

            velocity.ParseFromString(data[1:])
            #print("received message: %s" % data)
            print("received message:")
            print("Length of message: " + str(len(data)))

            print ("X: "+str(velocity.x))
            print ("Z: "+ str(velocity.y))
            MyMotors.RunTest()
            #MyMotors.setSpeedsVW_IPS(velocity.x, velocity.z)
        else:
            print("else")
            print (data)
            for i in data:
                print(ord(i))
finally:
    MyMotors.setSpeeds(0,0)
    print >>sys.stderr, 'shutting down servos'
