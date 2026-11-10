"""Compare spin, pivot, and arc turns on a SPIKE Prime robot."""

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
drive_base.settings(250, 500, 120, 240)

# 1. Spin: wheels travel opposite ways; robot center stays nearly in place.
drive_base.turn(90)
wait(1000)

# Return to the starting heading.
drive_base.turn(-90)
wait(1000)

# 2. Pivot: inside wheel stays approximately still.
# Radius is measured from the midpoint between the wheels.
drive_base.arc(radius=AXLE_TRACK_MM / 2, angle=90)
wait(1000)

# 3. Wide arc: both wheels move forward at different speeds.
drive_base.arc(radius=-250, angle=90)
