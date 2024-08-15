import pygame
import random
import board
import pacMan


class Ghost:
    def __init__(self, start_position, size):
        self.position = start_position
        self.size = size
        self.direction = pygame.Vector2(0, 0)
        self.speed = 0.8

        # Load Pac-Man Ghost character
        self.ghostChar = pygame.image.load("redGhost.png")  # Replace with actual path to Ghost pictures
        self.ghostChar = pygame.transform.scale(self.ghostChar, (size, size))

    def random_direction(self, board):
        possible_directions = [pygame.Vector2(0, -1), pygame.Vector2(0, 1), pygame.Vector2(-1, 0), pygame.Vector2(1, 0)]
        random.shuffle(possible_directions)

        for direction in possible_directions:
            new_position = self.position + direction * self.speed
            row, col = int(new_position.y), int(new_position.x)
            if board.layout[row][col] != '#':  # collision with a wall
                self.direction = direction  # assign new direction
                break

    def move(self, board):
        if self.direction.length_squared() == 0 or random.random() < 0.1:  # Change direction randomly
            self.random_direction(board)

        new_position = self.position + self.direction

        # Check for left warp
        if self.position.x < 0:
            self.position.x = board.width - 1

        # Check for right warp
        if self.position.x >= board.width:
            self.position.x = 0

        row, col = int(new_position.y), int(new_position.x)

        if 0 <= row < board.height and 0 <= col < board.width:
            if board.layout[row][col] != '#':  # move in new direction
                self.position = new_position

    def draw(self, screen):
        x = int(self.position.x * self.size)
        y = int(self.position.y * self.size)
        screen.blit(self.ghostChar, (x, y))
