class MotorBike:
    def __init__(self, gear = 4, speed = 120):
        self.gear = gear
        self.speed = speed

    def __repr__(self):
        return repr((self.gear, self.speed))

honda = MotorBike(6, 240)
yamaha = MotorBike()

print(yamaha)
print(honda)
