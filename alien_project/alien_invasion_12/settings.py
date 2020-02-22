# 创建设置类

class Settings():
    '''存储《外星人入侵》的所有设置类'''

    def __init__(self):
        '''初始化设置类'''

        # 屏幕设置
        self.screen_width = 760
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_speed_factor = 3
        self.bullet_width = 700
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 限制子弹的数量
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1表示向右，-1表示向左

        # 设置速度加快节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        # 记分数
        self.alien_point = 50

    def initialize_dynamic_settings(self):
        '''初始化随游戏的进行而变化'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)
