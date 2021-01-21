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

        # 子弹设置
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
