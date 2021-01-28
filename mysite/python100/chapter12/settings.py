class Settings():
    # 存储外星人入侵的所有设置类

    def __init__(self):
        # 初始化设置类

        # 屏幕设置
        self.screen_width = 1142
        self.screen_height = 630
        self.bg_color = (230, 230, 230)

        # 飞船的速度
        self.ship_speed_factor = 7.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 6
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # 外星人的速度
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 100

        # fleet_direction 1表示右移， -1表示左移
        self.fleet_direction = 1
