# 负责飞船的大部分行为

import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        '''初始化飞船的位置'''
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船
        self.image = pygame.image.load("/Users/hao/PycharmProjects/alien_project/alien_invasion_12/images/ship.bmp")
        self.rect = self.image.get_rect()  # 飞机的矩形
        self.screen_rect = self.screen.get_rect()  # 获得屏幕矩形尺寸

        # 将每首飞船放到底部居中
        self.rect.centerx = self.screen_rect.centerx  # x坐标，这个是坐标，只能是整数
        self.rect.bottom = self.screen_rect.bottom

        # 飞船的属性center中存储小数, 这个是存速度
        self.center = float(self.rect.centerx)

        # 飞船移动的标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        '''在指定位置上绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''根据移动的标志更新飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.centerx 更新rect对象，矩形
        self.rect.centerx = self.center

    def center_ship(self):
        '''让飞船回到中间'''
        self.center = self.screen_rect.centerx


