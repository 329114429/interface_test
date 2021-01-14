class Car():
    """汽车类"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """描述"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' ' + str(self.odometer_reading)
        return long_name

    def update_odometer(self, mileage):
        """里程数"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    def read_odometer(self):
        print("里程数： " + str(self.odometer_reading))

    def increment_odometer(self, miles):
        """增加指定量"""
        self.odometer_reading += miles


# my_car = Car('audi', 'a4', '2016')
# my_car.odometer_reading = 23
# my_car.update_odometer(24)
# my_car.increment_odometer(12)
# print(my_car.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# # my_tesla.describe_battery()
# my_tesla.battery_size.describe_battery()
# my_tesla.battery_size.get_range()
