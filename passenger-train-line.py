from pybricks.pupdevices import ColorSensor, DCMotor # ColorSensor instead of ColorDistanceSensor if using Mindstorms sensor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

motor = DCMotor(Port.A)
sensor = ColorSensor(Port.B) # ColorSensor instead of ColorDistanceSensor if using Mindstorms sensor

station_stop_time_ms = 5000
eol_stop_time_ms = 5000
forward_speed = 50
check_color_interval_ms = 50
wait_to_pass_overshot_color = 2000
brake_pause_ms = 100

def stop():
    motor.stop()
    wait(brake_pause_ms)
    motor.brake()

def reverseSpeed():
    global forward_speed
    forward_speed = forward_speed * (-1)

def handleTrainMovement():
    stop()
    wait(station_stop_time_ms)
    motor.dc(forward_speed)
    wait(wait_to_pass_overshot_color)

motor.dc(forward_speed)

while True:
    color = sensor.color()

    print("looking for GREEN Or REDs")
    if (color == Color.GREEN) or (color == Color.RED):
        print(" %r detected, stopping at station, and reversing" % (color))
        reverseSpeed()
        handleTrainMovement()

    print("looking for YELLOW")
    if color == Color.YELLOW:
        print("YELLOW detected, at station, stopping and continuing")
        handleTrainMovement()
   
    wait(check_color_interval_ms)