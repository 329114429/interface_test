import pygame


class Ship():

    def __init__(self, screen):
        # 初始化飞船并设置其初始位置
        self.screen = screen

        # 加载飞船图像并获取其外矩形
        self.image = pygame.image.load("/Users/hao/PycharmProjects/mysite/python100/chapter12/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # x中心
        self.rect.bottom = self.screen_rect.bottom  # 底部

    def blitme(self):
        # 在指定的位置绘制飞船， blit 块的意思
        self.screen.blit(self.image, self.rect)
