from python100.chapter9.electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()
