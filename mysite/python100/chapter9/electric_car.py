from python100.chapter9.car import Car


class Battery():
    """电车的类"""

    def __init__(self, battery_size=70):
        self.battery = battery_size

    def describe_battery(self):
        """描述电量"""
        print("电量_：" + str(self.battery))

    def get_range(self):
        """里程数"""
        range = 0
        if self.battery == 70:
            range = 240
        elif self.battery == 80:
            range = 270

        message = "this car can go approximately " + str(range)
        print(message)


class ElectricCar(Car):
    """继承Car,电动车"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = Battery()

    def describe_battery(self):
        print("电量：" + str(self.battery_size))

    def fill_gas_tank(self):
        """电车没有邮箱"""
        print("This car doesn't need a gas tank!")
