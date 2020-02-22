# 创建子弹类

import pygame
from pygame.sprite import Sprite  # pygame Sprite类，精灵


class Bullet(Sprite):
    '''一个队飞船发射的子弹类'''

    def __init__(self, ai_settings, screen, ship):
        '''在飞船的所处的位置创建一个子弹对象'''
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0，0）处设置一个子弹的矩形，然后在设置位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示子弹的的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.bullet_speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        # 更新子弹位置的最小值
        self.y -= self.bullet_speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
