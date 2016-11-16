"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: PUT-YOUR-NAMES_HERE (all of them).

The primary author of this module is: PUT-YOUR-NAME-HERE.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.


import time
import random
import m0
import tkinter
from tkinter import ttk














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
    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid(row=1, column=0)


    label1 = ttk.Label(main_frame, text='Number of Notes')
    label1.grid()
    dc.entry_box1 = ttk.Entry(main_frame, text='Number of Notes')
    dc.entry_box1.grid()
# You will need a integer for this entry box for how many notes you wanna play.


    label2 = ttk.Label(main_frame, text='length of Time')
    label2.grid()
    dc.entry_box2 = ttk.Entry(main_frame, text='length of Time')
    dc.entry_box2.grid()
# You will need a integer for this entry box for how long each notes you wanna play.

    label3 = ttk.Label(main_frame, text='Range of Time')
    label3.grid()
    dc.entry_box3 = ttk.Entry(main_frame, text='Range of Time')
    dc.entry_box3.grid()
# You will need a integer for this entry box for how long you wanna play for total.


    label4 = ttk.Label(main_frame, text='Name of File')
    label4.grid()
    dc.entry_box4 = ttk.Entry(main_frame, text='Name of File')
    dc.entry_box4.grid()
# You will name whatever you want to a file, but remember you need add".txt" at the end.


    button_play_random_notes = ttk.Button(main_frame, text='Play random notes')
    button_play_random_notes['command'] = lambda: songs_playing(dc)
    button_play_random_notes.grid()
# Button that uses the function"songs_playing", which play radom notes.


    button_play_random_notes_for_random_time = ttk.Button(main_frame, text='Play random notes for random time')
    button_play_random_notes_for_random_time['command'] = lambda: songs_playing_randomly(dc)
    button_play_random_notes_for_random_time.grid()
# Button that uses the function "songs_playing" for random time on each note.


    button_Compose_music = ttk.Button(main_frame, text='Compose music and dance with light on')
    button_Compose_music ['command'] = lambda: songs_composing(dc)
    button_Compose_music .grid()
# Button that uses "songs_composing", which makes robots to compose its own music.


    button_using_camera = ttk.Button(main_frame, text='usingcameratohitobject')
    button_using_camera['command'] = lambda: usingcameratohitobject(dc)
    button_using_camera.grid()
# Button that uses"usingcameratohitobject", which makes robot to find object and hit it.


    button_read_file = ttk.Button(main_frame, text='Read File')
    button_read_file['command'] = lambda: reading(dc, dc.entry_box4.get())
    button_read_file.grid()

# Button that uses"reading", which means reading the file.
# When you finish the requirements below, you can do it.
# Make sure your file is not blank.



    button_record_file = ttk.Button(main_frame, text='Record File')
    button_record_file['command'] = lambda: writing(root, dc, dc.entry_box4.get())
    button_record_file.grid()
# Button that uses "writing", which means record the movements.
# Remember to press space to stop your song.
# Remember to press Z and then space to stop your movements






def songs_playing(dc):

    notes = []
    N = int(dc.entry_box1.get())
    Time1 = int(dc.entry_box2.get())
    Time2 = Time1

    for k in range(N):
        randomnumber = int(random.randrange(1, 120))  # play randomly from 1 to 120, because the sounds below 120 is more ''hearable''
        notes = notes + [randomnumber] + [999999]

    for k in range(N * 2):

        if notes[k] != 999999:
            print(notes[k])
            dc.robot.buzzer.play_tone(notes[k])
            Time = Time1 + (Time2 - Time1) * (random.random())
            print(Time)
            time.sleep(Time)

        else:
            dc.robot.buzzer.play_tone(0)
            time.sleep(0.01)  # prevent clipp

        dc.robot.buzzer.stop()


def songs_playing_randomly(dc):
    notes = []
    N = int(dc.entry_box1.get())
    Time1 = int(dc.entry_box3.get())


    for k in range(N):
        randomnumber = int(random.randrange(1, 120))  # play randomly from 1 to 120, because the sounds below 120 is more ''hearable''
        notes = notes + [randomnumber] + [999999]

    for k in range(N * 2):

        if notes[k] != 999999:
            print(notes[k])
            dc.robot.buzzer.play_tone(notes[k])
            dc.robot.led.turn_on()

            if k == (N * 2) - 2:
                Time = Time1

            else:
                Time = Time1 * (random.random())
                Time1 = Time1 - Time
            print(Time)
            time.sleep(Time)

        else:
            dc.robot.buzzer.play_tone(0)
            time.sleep(0.01)  # prevent clipp

        dc.robot.buzzer.stop()
        dc.robot.led.turn_off()


def songs_composing(dc):
    k = random.randrange(0, 2)
    ryhme1 = ([0.5, 0.25, 0.25, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5], [0.5, 0.25, 0.25, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5])
    # ryhme2 = [(0.5, 0.5, 0.5, 0.5, 0.5, 0.5), (0.5, 0.5, 0.5, 0.5, 0.5, 1)]
    # ryhme3 = [(0.5, 0.5, 1, 0.5, 1, 1), (3, 1, 1, 0.5, 1, 1)]
    list1 = (58, 55, 21, 50, 19, 28, 15, 59, 56, 58, 21, 24, 19)
    # list2 = (28, 27, 55, 56, 60, 61, 49, 37, 36, 33, 33, 30)
    # list3 = ()




    for a in range(len(ryhme1[random.randrange(0, 2)])):


        dc.robot.buzzer.play_tone(random.choice(list1))  # compose music by ramdomly choose ryhme and sounds
        dc.robot.motor_controller.drive_pwm(random.randrange(-100, 100), random.randrange(-100, 100))  # dancing while composing music
        time.sleep(ryhme1[k][a % len(ryhme1[k])])
        dc.robot.buzzer.stop()
        dc.robot.led.turn_on()  # shinning while composing music

    dc.robot.motor_controller.drive_pwm(0, 0)
    dc.robot.led.turn_off()



def say_sorry_when_strike_others(dc):
    if dc.robot.sensor_reader.left_bump_sensor.read() == 0:
        dc.robot.buzzer.play_tone()

    elif dc.robot.sensor_reader.right_bump_sensor() == 0:
        dc.robot.buzzer.play_tone()

# If robot strike someone, it will make some sounds
'''
def go_to_the_colored_block(dc):
    x=dc.robot.camera.get_block()
    while True:
   '''


def usingcameratohitobject(dc):
    block = dc.robot.camera.get_block()

    while block is None:
        block = dc.robot.camera.get_block()
        dc.robot.motor_controller.drive_pwm(60, -60)
        time.sleep(0.1)
        dc.robot.motor_controller.drive_pwm(0, 0)
        time.sleep(0.1)

    print(block.x, block.y, block.width, block.height)

    dc.robot.motor_controller.drive_pwm(100, 100)
    time.sleep(5)
    dc.robot.motor_controller.drive_pwm(0, 0)

def reading(dc, NameOfFile):
    f = open(NameOfFile, 'r')
# open or make a file that can record my movements

    s = f.read()
    f.close()
    for k in range(len(s)):
        print(s[k], end='')

    print()
    speed = 40
    def go_left(dc):
        dc.robot.motor_controller.drive_pwm(0, speed)
        time.sleep(1)

    def go_forward(dc):
        dc.robot.motor_controller.drive_pwm(speed, speed)
        time.sleep(1)

    def go_right(dc):
        dc.robot.motor_controller.drive_pwm(speed, 0)
        time.sleep(1)

    def go_backward(dc):
        dc.robot.motor_controller.drive_pwm(-(speed), -(speed))
        time.sleep(1)

    def go_stop(dc):
        dc.robot.motor_controller.stop()
        time.sleep(1)

    def do(dc):
        dc.robot.buzzer.play_tone(43)
        time.sleep(0.8)
        dc.robot.buzzer.stop()

    def re(dc):
        dc.robot.buzzer.play_tone(45)
        time.sleep(0.8)
        dc.robot.buzzer.stop()

    def mi(dc):
        dc.robot.buzzer.play_tone(47)
        time.sleep(0.8)
        dc.robot.buzzer.stop()

    def fa(dc):
        dc.robot.buzzer.play_tone(48)
        time.sleep(0.8)
        dc.robot.buzzer.stop()

    def so(dc):
        dc.robot.buzzer.play_tone(50)
        time.sleep(0.8)
        dc.robot.buzzer.stop()

    def la(dc):
        dc.robot.buzzer.play_tone(52)
        time.sleep(0.8)
        dc.robot.buzzer.stop()

    def xi(dc):
        dc.robot.buzzer.play_tone(54)
        time.sleep(0.8)
        dc.robot.buzzer.stop()

    def h_do(dc):
        dc.robot.buzzer.play_tone(55)
        time.sleep(0.8)
        dc.robot.buzzer.stop()

    def h_re(dc):
        dc.robot.buzzer.play_tone(57)
        time.sleep(0.8)
        dc.robot.buzzer.stop()
# Read file by playing 0.8s for each notes and moving 1.0s for each movements.


    for k in range(len(s)):
        if s[k] == 'w':
            go_forward(dc)
        elif s[k] == 's':
            go_backward(dc)
        elif s[k] == 'a':
            go_left(dc)
        elif s[k] == 'd':
            go_right(dc)
        elif s[k] == 'z':
            go_stop(dc)
        elif s[k] == 'r':
            do(dc)
        elif s[k] == 't':
            re(dc)
        elif s[k] == 'y':
            mi(dc)
        elif s[k] == 'u':
            fa(dc)
        elif s[k] == 'i':
            so(dc)
        elif s[k] == 'o':
            la(dc)
        elif s[k] == 'p':
            xi(dc)
        elif s[k] == '[':
            h_do(dc)
        elif s[k] == ']':
            h_re(dc)
# When read the file, the robot will make response basic on the movements above.

def writing(root, dc, NameOfFile):
    f = open(NameOfFile, 'w')

    speed = 40
    def go_left(dc):
        dc.robot.motor_controller.drive_pwm(0, speed)
        time.sleep(1)
        f.write('a')

    def go_forward(dc):
        dc.robot.motor_controller.drive_pwm(speed, speed)
        time.sleep(1)
        f.write('w')

    def go_right(dc):
        dc.robot.motor_controller.drive_pwm(speed, 0)
        time.sleep(1)
        f.write('d')

    def go_backward(dc):
        dc.robot.motor_controller.drive_pwm(-(speed), -(speed))
        time.sleep(1)
        f.write('s')

    def go_stop(dc):
        dc.robot.motor_controller.stop()
        time.sleep(1)
        f.write('z')

    def do(dc):
        dc.robot.buzzer.play_tone(43)
        f.write('r')

    def re(dc):
        dc.robot.buzzer.play_tone(45)
        f.write('t')

    def mi(dc):
        dc.robot.buzzer.play_tone(47)
        f.write('y')

    def fa(dc):
        dc.robot.buzzer.play_tone(48)
        f.write('u')

    def so(dc):
        dc.robot.buzzer.play_tone(50)
        f.write('i')

    def la(dc):
        dc.robot.buzzer.play_tone(52)
        f.write('o')

    def xi(dc):
        dc.robot.buzzer.play_tone(54)
        f.write('p')

    def h_do(dc):
        dc.robot.buzzer.play_tone(55)
        f.write('[')

    def h_re(dc):
        dc.robot.buzzer.play_tone(57)
        f.write(']')


# If the operator presses the key, the movements will be recorded by the opened file.


    root.bind_all('<KeyRelease>', lambda _: dc.robot.buzzer.stop())
    root.bind_all('<Key-r>', lambda _:do(dc))
    root.bind_all('<Key-t>', lambda _:re(dc))
    root.bind_all('<Key-y>', lambda _:mi(dc))
    root.bind_all('<Key-u>', lambda _:fa(dc))
    root.bind_all('<Key-i>', lambda _:so(dc))
    root.bind_all('<Key-o>', lambda _:la(dc))
    root.bind_all('<Key-p>', lambda _:xi(dc))
    root.bind_all('<Key-[>', lambda _:h_do(dc))
    root.bind_all('<Key-]>', lambda _:h_re(dc))
    root.bind_all('<Key-space>', lambda _:f.close())
    root.bind_all('<Key-a>', lambda _:go_left(dc))
    root.bind_all('<Key-w>', lambda _:go_forward(dc))
    root.bind_all('<Key-s>', lambda _:go_backward(dc))
    root.bind_all('<Key-d>', lambda _:go_right(dc))
    root.bind_all('<Key-z>', lambda _:go_stop(dc))
# bind all the movements to the corresponding key
# When release the key, stop


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
   m0.main()
