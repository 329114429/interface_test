import datetime
import time


def current_time():
    current_day = datetime.date.today()
    # current_time = datetime.datetime.now()
    print(current_day)


if __name__ == '__main__':
    current_time()
