import pygame
import sys
from screen import start_screen
from board import Board, default_layout
from pacMan import PacMan
from ghost import Ghost


class Game:
    def __init__(self, screen):
        self.clock = pygame.time.Clock()
        self.screen = screen
        screen_width, screen_height = screen.get_size()
        self.board = Board(default_layout, screen_width, screen_height, self)  # Pass screen dimensions to Board
        self.pacman = PacMan(pygame.Vector2(1, 1), self.board.tile_size)  # start pos for PacMan
        # self.ghosts = [Ghost(pygame.Vector2(16, 13), self.board.tile_size)]  # Example start positions
        self.ghosts = [Ghost(pygame.Vector2(10, 11), self.board.tile_size)]  # Example start positions

        # for score keeping
        self.score = 0
        self.lives = 4

    def update_state(self):
        # Placeholder for game update logic

        # Get user input (ensure it's inside the loop)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.pacman.handle_input()
        self.pacman.move(self.board)
        print(f"Pac-Man Position: {self.pacman.position}")

        for ghost in self.ghosts:
            ghost.update()
            ghost.move(self.board)

        self.check_collisions()

        print(f"The score is {self.score}")

    def check_collisions(self):
        pos = self.pacman.position
        for ghost in self.ghosts:
            if pos == ghost.position:
                if ghost.vulnerable:
                    self.eat_ghost(ghost)
                else:
                    self.lives -= 1
                    self.reset_positions()
            print("Collision Detected")

    def reset_positions(self):
        self.pacman.position = pygame.Vector2(1, 1)
        for ghost in self.ghosts:
            ghost.position = pygame.Vector2(10, 10)  # Reset ghost positions

    def eat_ghost(self, ghost):
        if ghost.vulnerable:
            self.ghosts.remove(ghost)
            self.score += 100  # Increase score for eating ghosts

    def make_ghosts_vulnerable(self):
        for ghost in self.ghosts:
            ghost.make_vulnerable(200)

        return True
# 11-16
    def draw(self):
        # Placeholder for game drawing logic
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)  # Draw the board
        self.pacman.draw(self.screen)
        for ghost in self.ghosts:
            ghost.draw(self.screen)

        pygame.display.flip()


def main():
    while True:
        start_screen(screen)

        game = Game(screen)

        while True:
            game.update_state()
            game.draw()
            pygame.display.flip()
            pygame.time.Clock().tick(20)


if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pac-Man")
    main()
