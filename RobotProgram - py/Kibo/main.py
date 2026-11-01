from Robot import Robot
import time

robot = Robot("00:16:53:82:FA:E4")

while True:
    print((robot.Sensor2.distance)* 10)

    time.sleep(1)
