import pygame.ftfont


class Scoreboard():
    '''统计得分类'''

    def __init__(self, ai_settings, screen, stats):
        '''初始化得分及属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 得分显示字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图形
        self.prep_score()

    def prep_score(self):
        '''得分渲染一副图像'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)  # stats.score 转化为字符串
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 得分显示在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''在屏幕上显示'''
        self.screen.blit(self.score_image, self.score_rect)  # 图像显示，传递到指定的score_rect位置
