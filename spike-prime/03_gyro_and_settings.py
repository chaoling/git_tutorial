"""Gyro-assisted DriveBase example with separate accel/decel settings."""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait


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

# Keep the whole robot still until the hub's IMU is calibrated.
hub.display.char("G")
while not hub.imu.ready():
    wait(100)

drive_base.use_gyro(True)
drive_base.reset(distance=0, angle=0)

# Each tuple is (acceleration, deceleration).
drive_base.settings(
    straight_speed=250,
    straight_acceleration=(500, 400),
    turn_rate=120,
    turn_acceleration=(240, 180),
)

hub.display.char("R")
drive_base.straight(600)
drive_base.turn(90)
drive_base.straight(300)

print("Distance:", drive_base.distance(), "mm")
print("Heading:", drive_base.angle(), "degrees")
