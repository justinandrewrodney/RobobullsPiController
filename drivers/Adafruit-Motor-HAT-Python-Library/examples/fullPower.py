#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
Motor1 = mh.getMotor(1)
Motor2 = mh.getMotor(2)
Motor3 = mh.getMotor(3)
Motor4 = mh.getMotor(4)
# set the speed to start, from 0 (off) to 255 (max speed)


Motor1.run(Adafruit_MotorHAT.FORWARD);
Motor1.setSpeed(255)

Motor2.run(Adafruit_MotorHAT.BACKWARD);
Motor2.setSpeed(255)

Motor3.run(Adafruit_MotorHAT.FORWARD);
Motor3.setSpeed(255)

Motor4.run(Adafruit_MotorHAT.BACKWARD);
Motor4.setSpeed(255)
time.sleep(10)
# turn on motor
Motor1.run(Adafruit_MotorHAT.RELEASE);
Motor2.run(Adafruit_MotorHAT.RELEASE);
Motor3.run(Adafruit_MotorHAT.RELEASE);
Motor4.run(Adafruit_MotorHAT.RELEASE);


Motor1.run(Adafruit_MotorHAT.BACKWARD);
Motor1.setSpeed(255)

Motor2.run(Adafruit_MotorHAT.FORWARD);
Motor2.setSpeed(255)

Motor3.run(Adafruit_MotorHAT.BACKWARD);
Motor3.setSpeed(255)

Motor4.run(Adafruit_MotorHAT.FORWARD);
Motor4.setSpeed(255)
time.sleep(10)
# turn on motor
Motor1.run(Adafruit_MotorHAT.RELEASE);
Motor2.run(Adafruit_MotorHAT.RELEASE);
Motor3.run(Adafruit_MotorHAT.RELEASE);
Motor4.run(Adafruit_MotorHAT.RELEASE);