"""First SPIKE Prime DriveBase program.

Check every port, direction, and measurement before placing the robot on a table.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase


WHEEL_DIAMETER_MM = 56
AXLE_TRACK_MM = 112

hub = PrimeHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)

drive_base = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER_MM,
    axle_track=AXLE_TRACK_MM,
)

drive_base.settings(300, 600, 180, 360)

drive_base.straight(500)
drive_base.turn(90)
drive_base.straight(250)
drive_base.turn(-90)
drive_base.straight(-200)
