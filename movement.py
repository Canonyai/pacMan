import pygame


class Movement:
    def move(self, direction):
        possible_directions = {'down': pygame.Vector2(0, -1),
                               'up': pygame.Vector2(0, 1),
                               'left': pygame.Vector2(-1, 0),
                               'right': pygame.Vector2(1, 0)}
