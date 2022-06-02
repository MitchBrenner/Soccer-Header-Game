import pygame
import random


class Cleat:

    def __init__(self):
        self.image = pygame.image.load('images/soccer_cleat.png')
        self.speed = random.randint(20, 25)
        self.y_pos = random.randint(-200, -50)
        self.x_pos = random.randint(200, 1000)
        self.is_active = True


    def get_img(self):
        self.image = pygame.transform.scale(self.image, (130, 130))
        return self.image


    def drop_cleat(self):
        if self.y_pos > 800:
            print("missed")
            self.is_active = False
        else:
            self.y_pos += self.speed


    def get_x_y_coord(self):
        return self.x_pos, self.y_pos