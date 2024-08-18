from pellets import Pellet
import pygame


class PowerPellet(Pellet):
    def __init__(self, position, tile_size):
        super().__init__(position, tile_size)

    def draw(self, screen):
        x = int(self.position.x * self.size) + self.size // 2
        y = int(self.position.y * self.size) + self.size // 2
        pygame.draw.circle(screen, (255, 255, 0), (x, y), self.size // 3)

    def activate_power(self, game):
        # Logic to make ghosts vulnerable
        game.make_ghosts_vulnerable()
