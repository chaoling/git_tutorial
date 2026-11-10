"""First hub test. Upload with pybricksdev, or use the Pybricks VS Code task.

This program changes the hub light and prints a message without moving motors.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Color

hub = PrimeHub()
hub.light.on(Color.GREEN)
print("Hello, SPIKE Prime!")
