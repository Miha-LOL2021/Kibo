import ev3_dc as ev3
from ev3_dc.ev3 import Sensors


class Robot:
    def __init__(self, macAddress):
        self.Robot = ev3.EV3(protocol=ev3.BLUETOOTH, host=macAddress)

        self.MotorA = ev3.Motor(ev3.PORT_A, ev3_obj=self.Robot, speed=5)
        self.MotorB = ev3.Motor(ev3.PORT_B, ev3_obj=self.Robot, speed=100)

        self.Sensor1 = ev3.Ultrasonic(ev3.PORT_1, ev3_obj=self.Robot)
        self.Sensor2 = ev3.Ultrasonic(ev3.PORT_2, ev3_obj=self.Robot)
        self.Sensor3 = ev3.Ultrasonic(ev3.PORT_3, ev3_obj=self.Robot)
        self.Sensor4 = ev3.Ultrasonic(ev3.PORT_4, ev3_obj=self.Robot)

        print("The robot connect")

    def GiveFood(self, gramOfFood):
        distance = self.Sensor1.distance

        if (10 < distance < 50):
            self.MotorA.move_by(degrees=30 * round((gramOfFood / 5))).start(thread=False)





