import pygame
from alien_invasion_12.settings import Settings
from alien_invasion_12.ship import Ship
from alien_invasion_12 import game_functions
from pygame.sprite import Group
from alien_invasion_12.alien import Alien
from alien_invasion_12.game_stats import GameStats
from alien_invasion_12.button import Button
from alien_invasion_12.scoreboard import Scoreboard


def run_game():
    '''初始化一个游戏，并创建一个游戏对象'''
    pygame.init()

    ai_settings = Settings()  # 设置类的对象

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)  # 设置宽高
    )

    pygame.display.set_caption('Alien_invasion')

    # 创建一个play按钮
    play_button = Button(ai_settings, screen, "play")

    # 创建一个飞船
    ship = Ship(ai_settings, screen)

    # 创建一组子弹,需到导入pygame.sprite 类
    bullets = Group()

    # 创建一个外星人
    alien = Alien(ai_settings, screen)

    # 创建外星人群组
    aliens = Group()
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个储存游戏的信息
    stats = GameStats(ai_settings)

    # 创建一个得分牌
    scoreboard = Scoreboard(ai_settings, screen, stats)

    # 开始游戏的主循环
    while True:
        # 鼠标和按键事件
        game_functions.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()

            game_functions.update_bullets(ai_settings, screen, stats, scoreboard, ship, bullets, aliens)

            game_functions.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        game_functions.update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button)


run_game()
