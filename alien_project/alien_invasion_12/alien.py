# 创建外星人类

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''表示单个外星人的类'''

    def __init__(self, ai_settings, screen):
        '''初始化外星人并设置位置'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图形，并设置rect属性
        self.image = pygame.image.load('/Users/hao/PycharmProjects/alien_project/alien_invasion_12/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人初始位置在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精准位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''外星人位于边缘返回'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''更新外星人的位置，向右移动外星人'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


