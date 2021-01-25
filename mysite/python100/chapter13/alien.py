import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # 单个外星人的类

    def __init__(self, ai_settings, screen):
        # 初始化外星人并设置其位置
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人凸显，并设置rect属性
        self.image = pygame.image.load("/Users/hao/PycharmProjects/mysite/python100/chapter13/images/alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        # 在指定位置绘制外星人
        self.screen.blit(self.image, self.rect)
