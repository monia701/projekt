import pygame

class GameObject:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def update(self):
        pass

    def draw(self, screen):
        pass
