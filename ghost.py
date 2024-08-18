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
        self.vulnerable_timer = 0
        self.vulnerable = False

        # Load Pac-Man Ghost character
        self.normalGhostChar = pygame.image.load("redGhost.png")  # Replace with actual path to Ghost pictures
        self.scaredGhostChar = pygame.image.load("whiteGhost.png")
        self.ghostChar = pygame.transform.scale(self.normalGhostChar, (size, size))

    def random_direction(self, board):
        possible_directions = [pygame.Vector2(0, -1), pygame.Vector2(0, 1), pygame.Vector2(-1, 0), pygame.Vector2(1, 0)]
        random.shuffle(possible_directions)

        for direction in possible_directions:
            new_position = self.position + direction * self.speed
            row, col = int(new_position.y), int(new_position.x)
            if board.layout[row][col] != '#':  # collision with a wall
                self.direction = direction  # assign new direction
                break

    def make_vulnerable(self, duration):
        self.vulnerable = True
        self.vulnerable_timer = duration
        self.ghostChar = pygame.transform.scale(self.scaredGhostChar, (self.size, self.size))

    def update(self):
        if self.vulnerable:
            self.vulnerable_timer -= 1
            if self.vulnerable_timer <= 0:
                self.vulnerable = False
                self.ghostChar = pygame.transform.scale(self.normalGhostChar, (self.size, self.size))

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
