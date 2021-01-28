import pygame
from pygame.sprite import Group

from python100.chapter12.settings import Settings
from python100.chapter12.ship import Ship
from python100.chapter12 import game_functions as gf
from python100.chapter13.alien import Alien
from python100.chapter13.game_stats import GameStats


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

    # 创建一个外星人编组
    aliens = Group()

    # 创建一个存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()

            # 子弹的更新
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            # 更新外星人
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 每次循环都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
