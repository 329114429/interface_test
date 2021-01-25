import pygame
from pygame.sprite import Group

from python100.chapter12.settings import Settings
from python100.chapter12.ship import Ship
from python100.chapter12 import game_functions as gf
from python100.chapter13.alien import Alien


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 按照16：9
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个子弹组
    bullets = Group()

    alien = Alien(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        # 子弹的更新
        gf.update_bullets(bullets)

        # 每次循环都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
