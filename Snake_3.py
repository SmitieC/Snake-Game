import time
import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 720))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - Created by Conor")

time.sleep(5)
pygame.quit()
quit()
