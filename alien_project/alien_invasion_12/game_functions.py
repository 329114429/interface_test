# functions class 事件类

import sys
import pygame
from alien_invasion_12.bullet import Bullet
from alien_invasion_12.alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''响应按键事件'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，加入到编组中
        fire_bullet(ai_settings, screen, ship, bullets)  # 调用下面的子弹射击方法
    elif event.key == pygame.K_q:  # 按键q 退出程序
        sys.exit()


def check_keyup_events(event, ship):
    '''响应松开事件'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    '''鼠标和按键事件'''
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:  # 按下，移动
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:  # 松开，停止
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''玩家点击play按钮时开始'''

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

    # 清空外星人和子弹
    aliens.empty()
    bullets.empty()

    # 创建一排外星人,并让飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button):
    '''更新屏幕上的图像，切换到新屏幕'''

    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # 显示得分
    scoreboard.show_score()

    # 游戏处于非活跃状态
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, scoreboard, ship, bullets, aliens):
    '''更新子弹的位置和数量，删除消失的子弹'''
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(ai_settings, screen, stats, scoreboard, ship, bullets, aliens)


def check_bullet_alien_collision(ai_settings, screen, stats, scoreboard, ship, bullets, aliens):
    # 检查是否有子弹击中外星人，有就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_point * len(aliens)
            scoreboard.prep_score()

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    '''发射子弹'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    '''计算一行可以容纳多少外星人'''
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    '''计算屏幕能容纳多少行外星人'''
    available_space_y = int(ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''创建一个外星人'''
    alien = Alien(ai_settings, screen)

    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)  # x 的长度
    alien.rect.x = alien.x

    alien_height = alien.rect.height
    alien.rect.y = alien_height + (2 * alien_height * row_number)

    aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
    '''判断外星人是否到达边缘'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    '''检查外星人到达底部'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def change_fleet_direction(ai_settings, aliens):
    '''将整个外星人群下已，并改变方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def create_fleet(ai_settings, screen, ship, aliens):
    '''创建外星人组'''
    alien = Alien(ai_settings, screen)

    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建第一行并加入其中
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''检查外星人和飞船的碰撞,碰撞 - 1'''
    if stats.ship_left > 0:
        stats.ship_left -= 1

        # 清空外星人列表和子弹
        aliens.empty()
        bullets.empty()

        # 新建外星人和飞船
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂定0.5秒
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''更新外星人位置'''
    check_fleet_edges(ai_settings, aliens)

    aliens.update()

    # 检查外星人和飞船的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # 检查外星人是否到底部
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
