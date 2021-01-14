from python100.chapter9.car import Car

my_new = Car('audi', 'a4', 2016)
print(my_new.get_descriptive_name())
my_new.odometer_reading = 23
my_new.read_odometer()
