import pygame

import board


class PacMan:
    def __init__(self, start_position, size):
        self.size = size
        self.position = start_position
        self.direction = pygame.Vector2(0, 0)  # Initially stationary
        self.speed = 1

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

    # def move(self, board):
    #     # Calculate new position
    #     updated_position = self.position + self.direction * self.speed
    #     # updated_position = self.position + self.direction
    #
    #     # Check for left warp
    #     if self.position.x < 0:
    #         self.position.x = board.width - 1
    #
    #     # Check for right warp
    #     if self.position.x >= board.width:
    #         self.position.x = 0
    #
    #     # Check for wall collision
    #     row, col = int(updated_position.y), int(updated_position.x)
    #     if 0 <= row < board.height and 0 <= col < board.width:
    #         if board.layout[row][col] != '#':  # Can move if not hitting a wall
    #             self.position = updated_position
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

        # No collision, update position
        self.position = new_pos

    def draw(self, screen):
        x = int(self.position.x * self.size)
        y = int(self.position.y * self.size)
        screen.blit(self.pacManChar, (x, y))



