# 跟踪游戏信息的类

class GameStats():
    '''统计游戏信息'''

    def __init__(self, ai_settings):
        '''初始化统计信息'''
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        '''重置初始化信息'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
