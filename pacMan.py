import pygame

import board
from powerPellets import PowerPellet


class PacMan:
    def __init__(self, start_position, size):
        self.size = size
        self.position = start_position
        self.direction = pygame.Vector2(0, 0)  # Initially stationary
        self.speed = 1
        self.powerup = False

        # Load Pac-Man character
        self.pacManChar = pygame.image.load("pacman.gif")  # Replace with actual path to Pac-Man sprite
        self.pacManChar = pygame.transform.scale(self.pacManChar, (size, size))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = pygame.Vector2(0, -1)
        elif keys[pygame.K_DOWN]:
            self.direction = pygame.Vector2(0, 1)
        elif keys[pygame.K_LEFT]:
            self.direction = pygame.Vector2(-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.direction = pygame.Vector2(1, 0)

    def move(self, board):
        # Calculate new position
        new_pos = self.position + self.direction * self.speed

        # Check for left warp
        if new_pos.x < 0:
            new_pos.x = board.width - 1

        # Check for right warp
        if new_pos.x >= board.width:
            new_pos.x = 0

        # Check for wall collision
        new_rect = pygame.Rect(new_pos.x * self.size, new_pos.y * self.size, self.size, self.size)
        for row in range(board.height):
            for col in range(board.width):
                if board.layout[row][col] == '#':
                    wall_rect = pygame.Rect(col * self.size, row * self.size, self.size, self.size)
                    if new_rect.colliderect(wall_rect):
                        return  # Prevent movement

        # Check for collision with pellets to allow Pac-Man to eat them
        for pellet in board.pellets:
            pellet_rect = pygame.Rect(pellet.position.x * self.size, pellet.position.y * self.size, self.size,
                                      self.size)
            if new_rect.colliderect(pellet_rect) and not pellet.eaten:
                pellet.eaten = True
                board.pellets.remove(pellet)
                board.game.score += 10  # Increase the score or apply other logic

                if isinstance(pellet, PowerPellet):
                    pellet.activate_power(board.game)  # Activate power pellet effect
                    board.game.score += 10  # Regular pellet, increase score# No collision, update position

        # No collision, update position
        self.position = new_pos

    def draw(self, screen):
        x = int(self.position.x * self.size)
        y = int(self.position.y * self.size)
        screen.blit(self.pacManChar, (x, y))
