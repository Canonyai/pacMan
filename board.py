import pygame
from pellets import Pellet
from powerPellets import PowerPellet


class Board:
    def __init__(self, layout, screen_width, screen_height, game):
        self.layout = layout
        self.width = len(layout[0])
        self.height = len(layout)
        self.pellets = []  # pellets that'll be on the screen
        self.powerPellets = []  # power pellets
        self.game = game

        # Calculate the tile size to make the board fill the screen
        self.tile_size = min(screen_width // self.width, screen_height // self.height)

        # Initialize the pellets based on the layout
        for row_index, row in enumerate(self.layout):
            for col_index, object in enumerate(row):
                if object == '.':
                    position = pygame.Vector2(col_index, row_index)
                    self.pellets.append(Pellet(position, self.tile_size))
                elif object == 'o':
                    position = pygame.Vector2(col_index, row_index)
                    self.pellets.append(PowerPellet(position, self.tile_size))

    def draw(self, screen):
        for row_index, row in enumerate(self.layout):
            for col_index, item in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size

                if item == "#":
                    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, self.tile_size, self.tile_size))

                # elif item == "o":
                #     pygame.draw.circle(screen, (255, 255, 255), (x + self.tile_size // 2, y + self.tile_size // 2),
                #                        self.tile_size // 3)

        for pellet in self.pellets:
            pellet.draw(screen)
        for pellet in self.powerPellets:
            pellet.draw(screen)


# Example layout for the board
default_layout = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o####.#####.##.#####.####o#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ###--### ##.######",
    "######.## #      # ##.######",
    "       .   ######   .       ",
    "######.## #      # ##.######",
    "######.## ######## ##.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#o..##.......P  ......##..o#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]
