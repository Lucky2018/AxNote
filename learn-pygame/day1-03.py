# https://blog.csdn.net/zha6476003/article/details/82940350

import pygame
import sys

pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
color = (0, 0, 0)  # 设置颜色
ball = pygame.image.load('ball.png')  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域

speed = [1, 1]  # 设置移动的X轴、Y轴
while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
    ballrect = ballrect.move(speed)  # 移动小球
    screen.fill(color)  # 填充颜色(设置为0，执不执行这行代码都一样)
    screen.blit(ball, ballrect)  # 将图片画到窗口上
    pygame.display.flip()  # 更新全部显示

pygame.quit()  # 退出pygame