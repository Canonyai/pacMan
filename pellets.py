import pygame


class Pellet:
    def __init__(self, position, size):
        self.eaten = False
        self.position = position
        self.size = size

    def draw(self, screen):
        if self.eaten is False:
            x = int(self.position.x * self.size) + self.size // 2
            y = int(self.position.y * self.size) + self.size // 2
            pygame.draw.circle(screen, (255, 255, 255), (x, y), self.size // 6)
