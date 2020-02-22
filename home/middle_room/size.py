from middle_room.size_settings import Size_settings

bed = Size_settings()


def bed_size():
    center_size = (224 + 28 + 8.6 ) - 181
    print(center_size)


def bed_size_big():
    center_size_big = (215 + 2 * 8.6 + 40)
    print(center_size_big)


def main():
    bed_size()
    bed_size_big()


if __name__ == '__main__':
    main()
