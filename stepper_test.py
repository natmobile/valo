#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr = 0x60)

# Automatically disable motors on shutdown
def turnOffMotors():
  mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
  mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

# 200 steps/rev, motor port #1
motor_x = mh.getStepper(200, 1)

# 30 RPM
motor_x.setSpeed(30)

print("Single coil steps")
motor_x.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
motor_x.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

print("Double coil steps")
motor_x.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
motor_x.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

print("Interleaved coil steps")
motor_x.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)
motor_x.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)

print("Microsteps")
motor_x.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
motor_x.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
