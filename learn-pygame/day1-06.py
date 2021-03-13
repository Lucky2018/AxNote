# https://blog.csdn.net/zha6476003/article/details/82940350

# -*- coding:utf-8 -*-
import sys  # 导入sys模块
import pygame  # 导入pygame模块
import random


class Bird(object):
    """定义一个鸟类"""
    def __init__(self):
        """定义初始化方法"""
        pass

    def birdUpdate(self):
        pass


class Pipeline(object):
    """定义一个管道类"""
    def __init__(self):
        """定义初始化方法"""

    def updatePipeline(self):
        """水平移动"""


def createMap():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))  # 填充颜色(screen还没定义不要着急)
    screen.blit(background, (0, 0))  # 填入到背景
    pygame.display.update()  # 更新显示


if __name__ == '__main__':
    pygame.init()                           # 初始化pygame
    size = width, height = 400, 650         # 设置窗口大小
    screen = pygame.display.set_mode(size)  # 显示窗口
    clock = pygame.time.Clock()             # 设置时钟
    Pipeline = Pipeline()                   # 实例化管道类
    while True:
        clock.tick(60)                      # 每秒执行60次
        # 轮询事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # 如果检测到事件是关闭窗口
                sys.exit()

        background = pygame.image.load("image/background.png")  # 加载背景图片
        createMap()
    pygame.quit()  # 退出
