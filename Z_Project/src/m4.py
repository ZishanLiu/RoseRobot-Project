"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: PUT-YOUR-NAMES_HERE (all of them).

The primary author of this module is: lyum.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m2
import m3

import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb
import time

def my_frame(root, dc):
    """
    Constructs and returns a   ttk.Frame   on the given root window.
    The frame contains all of this module's widgets.
    Does NOT   grid   the Frame, since the caller will do that.
    Also sets up callbacks for this module's widgets.

    The first argument is the  root  window (a tkinter.Tk object)
    onto which the   ttk.Frame  returned from this function
    will be placed.  The second argument is the shared DataContainer
    object that is CONSTRUCTED in m0 but USED in m1, m2, m3 and m4.

    Preconditions:
      :type root: tkinter.Tk
      :type dc:   m0.DataContainer
    """
    frame = ttk.Frame(root, width=100, height=200)
    frame.grid()

    speedbutton = ttk.Button(frame, text='speed')
    speedbutton['command'] = (lambda:speed(dc))

    dc.speedentry = ttk.Entry(frame)
    dc.darkness = ttk.Entry(frame)
    dc.distanceleft = ttk.Entry(frame)
    dc.distanceright = ttk.Entry(frame)
    dc.distancemiddle = ttk.Entry(frame)
    dc.threshholdentry = ttk.Entry(frame)
    dc.errorentry = ttk.Entry(frame)
    dc.Pcontrolerrorentry = ttk.Entry(frame)
    dc.Polygonpointsentry = ttk.Entry(frame)


    bumpleftbutton = ttk.Button(frame, text='bumpleft')
    bumpleftbutton['command'] = (lambda:bumpleft(dc))
    bumprightbutton = ttk.Button(frame, text='bumpright')
    bumprightbutton['command'] = (lambda:bumpright(dc))
    bumpbothbutton = ttk.Button(frame, text='bumpboth')
    bumpbothbutton['command'] = (lambda:bumpboth(dc))
    reflectanceleftbutton = ttk.Button(frame, text='reflectanceleft')
    reflectanceleftbutton['command'] = (lambda:reflectanceleft(dc))
    reflectancerightbutton = ttk.Button(frame, text='reflectanceright')
    reflectancerightbutton['command'] = (lambda:reflectanceright(dc))
    reflectancemiddlebutton = ttk.Button(frame, text='reflectancemiddle')
    reflectancemiddlebutton['command'] = (lambda:reflectancemiddle(dc))
    proximityleftbutton = ttk.Button(frame, text='proximityleft')
    proximityleftbutton['command'] = (lambda:proximityleft(dc))
    proximityrightbutton = ttk.Button(frame, text='proximityright')
    proximityrightbutton['command'] = (lambda:proximityright(dc))
    proximitymiddlebutton = ttk.Button(frame, text='proximitymiddle')
    proximitymiddlebutton['command'] = (lambda:proximitymiddle(dc))
    BangBangbutton = ttk.Button(frame, text='BangBang')
    BangBangbutton['command'] = (lambda:BangBang(dc))
    Pcontrolbutton = ttk.Button(frame, text='Pcontrol')
    Pcontrolbutton['command'] = (lambda:Pcontrol(dc))
    Polygonleftbutton = ttk.Button(frame, text='Polygonleft')
    Polygonleftbutton['command'] = (lambda:Polygonleft(dc))
    Polygonrightbutton = ttk.Button(frame, text='Polygonright')
    Polygonrightbutton['command'] = (lambda:Polygonright(dc))
    ParallelParkbutton = ttk.Button(frame, text='Parallel Park')
    ParallelParkbutton['command'] = (lambda:ParallelPark(dc))




    speedbutton.grid(row=0, column=0)
    dc.speedentry.grid(row=0, column=1)
    bumpbothbutton.grid()
    bumpleftbutton.grid()
    bumprightbutton.grid()
    reflectanceleftbutton.grid()
    reflectancemiddlebutton.grid()
    reflectancerightbutton.grid()
    dc.darkness.grid(row=5, column=1)
    proximityleftbutton.grid()
    dc.distanceleft.grid(row=7, column=1)
    proximityrightbutton.grid()
    dc.distanceright.grid(row=8, column=1)
    proximitymiddlebutton.grid()
    dc.distancemiddle.grid(row=9, column=1)
    BangBangbutton.grid()
    dc.threshholdentry.grid(row=10, column=1)
    dc.errorentry.grid(row=11, column=1)
    Pcontrolbutton.grid()
    dc.Pcontrolerrorentry.grid(row=12, column=1)
    Polygonleftbutton.grid(row=0, column=3)
    dc.Polygonpointsentry.grid(row=0, column=4)
    Polygonrightbutton.grid(row=1, column=3)
    ParallelParkbutton.grid(row=2, column=3)


def speed(dc):
    myentry = dc.speedentry.get()
    speed = int(myentry)
    dc.robot.motor_controller.drive_pwm(speed, speed)

def bumpleft(dc):
    print('The left bumpsensor is on!')
    print(dc.robot.sensor_reader.left_bump_sensor.read())
    while True:
        if dc.robot.sensor_reader.left_bump_sensor.read() == 0:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break

def bumpright(dc):
    print('The right bumpsensor is on!')
    print(dc.robot.sensor_reader.right_bump_sensor.read())
    while True:
        if dc.robot.sensor_reader.right_bump_sensor.read() == 0 :
            dc.robot.motor_controller.drive_pwm(0, 0)
            break

def bumpboth(dc):
    print('Both bumpsensors are on!')
    print(dc.robot.sensor_reader.left_bump_sensor.read())
    print(dc.robot.sensor_reader.right_bump_sensor.read())
    while True:
        if dc.robot.sensor_reader.left_bump_sensor.read() == 0:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
        elif dc.robot.sensor_reader.right_bump_sensor.read() == 0:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def reflectanceleft(dc):
    print('The left reflectancesensor is on!')
    print(dc.robot.sensor_reader.left_reflectance_sensor.read())
    dark = dc.darkness.get()
    darknessthreshhold = int(dark)
    while True:
        if dc.robot.sensor_reader.left_reflectance_sensor.read() > darknessthreshhold:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def reflectanceright(dc):
    print('The right reflectancesensor is on!')
    print(dc.robot.sensor_reader.right_reflectance_sensor.read())
    dark = dc.darkness.get()
    darknessthreshhold = int(dark)
    while True:
        if dc.robot.sensor_reader.right_reflectance_sensor.read() > darknessthreshhold:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def reflectancemiddle(dc):
    dark = dc.darkness.get()
    darknessthreshhold = int(dark)
    print('The middle reflectancesensor is on!')
    print(dc.robot.sensor_reader.middle_reflectance_sensor.read())
    while True:
        if dc.robot.sensor_reader.middle_reflectance_sensor.read() > darknessthreshhold:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def proximityleft(dc):
    print('The left proximity sensor is on!')
    print(dc.robot.sensor_reader.left_proximity_sensor.read())
    distance = dc.distanceleft.get()
    d = int(distance)
    while True:
        if dc.robot.sensor_reader.left_proximity_sensor.read() > d:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def proximityright(dc):
    print('The right proximity sensor is on!')
    print(dc.robot.sensor_reader.right_proximity_sensor.read())
    distance1 = dc.distanceright.get()
    d1 = int(distance1)
    while True:
        if dc.robot.sensor_reader.right_proximity_sensor.read() > d1:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def proximitymiddle(dc):
    print('The middle proximity sensor is on!')
    print(dc.robot.sensor_reader.middle_proximity_sensor.read())
    distance2 = dc.distancemiddle.get()
    d2 = int(distance2)
    while True:
        if dc.robot.sensor_reader.middle_proximity_sensor.read() > d2:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def BangBang(dc):
    print('BangBang Going On!')
    thresh = dc.threshholdentry.get()
    error = dc.errorentry.get()
    thresh1 = int(thresh)
    error1 = int(error)
    dc.robot.motor_controller.drive_pwm(50, 50)
    print(dc.robot.sensor_reader.left_reflectance_sensor.read())
    print(dc.robot.sensor_reader.right_reflectance_sensor.read())
    while True:
        if dc.robot.sensor_reader.left_reflectance_sensor.read() < thresh1 - error1:
            dc.robot.motor_controller.drive_pwm(40, 10)
        if dc.robot.sensor_reader.right_reflectance_sensor.read() < thresh1 - error1:
            dc.robot.motor_controller.drive_pwm(10, 40)
        if dc.robot.sensor_reader.right_reflectance_sensor.read() < thresh1 - error1 and dc.robot.sensor_reader.left_reflectance_sensor.read() < thresh1 - error1:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def Pcontrol(dc):
    print('Pcontrol Going On!')
    myentry = dc.speedentry.get()
    speed = int(myentry)
    pcontrolerror = dc.Pcontrolerrorentry.get
    thresh = dc.threshholdentry.get()
    error = dc.errorentry.get()
    perror = int(pcontrolerror)
    thresh1 = int(thresh)
    error1 = int(error)
    dc.robot.motor_controller.drive_pwm(speed, speed)
    print(dc.robot.sensor_reader.left_reflectance_sensor.read())
    print(dc.robot.sensor_reader.right_reflectance_sensor.read())
    while True:
        if dc.robot.sensor_reader.left_reflectance_sensor.read() < thresh1 - error1:
            dc.robot.motor_controller.drive_pwm(speed + 0.05 * perror, speed)
        if dc.robot.sensor_reader.right_reflectance_sensor.read() < thresh1 - error1:
            dc.robot.motor_controller.drive_pwm(10, 40)
        if dc.robot.sensor_reader.right_reflectance_sensor.read() < thresh1 - error1 and dc.robot.sensor_reader.left_reflectance_sensor.read() < thresh1 - error1:
            dc.robot.motor_controller.drive_pwm(0, 0)
            break
def Polygonleft(dc):
    pointsget = dc.Polygonpointsentry.get()
    points = int(pointsget)
    myentry = dc.speedentry.get()
    speed = int(myentry)
    angle = (points - 2) * 180 / points
    print('The perimeter is', points * speed * 2)
    print('The lines needed are', points)
    print('The angle is', (points - 2) * 180 / points)
    for k in range(points):
        dc.robot.motor_controller.drive_pwm(speed, speed)
        time.sleep(3)
        dc.robot.motor_controller.drive_pwm(0, 100)
        time.sleep(0.0006 * angle)
    dc.robot.motor_controller.drive_pwm(0, 0)
def Polygonright(dc):
    pointsget = dc.Polygonpointsentry.get()
    points = int(pointsget)
    myentry = dc.speedentry.get()
    speed = int(myentry)
    print('The perimeter is', points * speed * 2)
    print('The lines needed are', points)
    print('The angle is', (points - 2) * 180 / points)
    for k in range(points):
        dc.robot.motor_controller.drive_pwm(speed, speed)
        time.sleep(2)
        dc.robot.motor_controller.drive_pwm(speed, 0)
        time.sleep(0.5)
    dc.robot.motor_controller.drive_pwm(0, 0)
def ParallelPark(dc):
    myentry = dc.speedentry.get()
    speed = int(myentry)
    dc.robot.motor_controller.drive_pwm(speed, speed)
    while True:
        if speed > 0:
            if  dc.robot.sensor_reader.left_proximity_sensor.read() > 300:
                dc.robot.motor_controller.drive_pwm(50, 50)
                time.sleep(0.5)
                dc.robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.01)
                dc.robot.motor_controller.drive_pwm(0, 100)
                time.sleep(0.7)
                dc.robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.01)
                dc.robot.motor_controller.drive_pwm(50, 50)
                time.sleep(1.2)
                dc.robot.motor_controller.drive_pwm(0, 0)
                break
            if  dc.robot.sensor_reader.right_proximity_sensor.read() > 300:
                dc.robot.motor_controller.drive_pwm(50, 50)
                time.sleep(0.4)
                dc.robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.01)
                dc.robot.motor_controller.drive_pwm(100, 0)
                time.sleep(0.9)
                dc.robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.01)
                dc.robot.motor_controller.drive_pwm(50, 50)
                time.sleep(1.2)
                dc.robot.motor_controller.drive_pwm(0, 0)
                break
        if speed < 0:
            if  dc.robot.sensor_reader.left_proximity_sensor.read() > 300:
                dc.robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.05)
                dc.robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.01)
                dc.robot.motor_controller.drive_pwm(0, -100)
                time.sleep(0.5)
                dc.robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.01)
                dc.robot.motor_controller.drive_pwm(-50, -50)
                time.sleep(0.8)
                dc.robot.motor_controller.drive_pwm(0, 0)
                break
            if  dc.robot.sensor_reader.right_proximity_sensor.read() > 300:
                dc.robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.05)
                dc.robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.01)
                dc.robot.motor_controller.drive_pwm(-105, 0)
                time.sleep(0.65)
                dc.robot.motor_controller.drive_pwm(0, 0)
                time.sleep(0.01)
                dc.robot.motor_controller.drive_pwm(-50, -50)
                time.sleep(0.8)
                dc.robot.motor_controller.drive_pwm(0, 0)
                break


























# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()
