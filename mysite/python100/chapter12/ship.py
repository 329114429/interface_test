import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外矩形
        self.image = pygame.image.load("/Users/hao/PycharmProjects/mysite/python100/chapter12/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # x中心
        self.rect.bottom = self.screen_rect.bottom  # 底部

        # 在飞船的属性centerx中存小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 根据移动标志调整位置
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        # 在指定的位置绘制飞船， blit 块的意思
        self.screen.blit(self.image, self.rect)
