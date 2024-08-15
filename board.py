import pygame


class Board:
    def __init__(self, layout, screen_width, screen_height):
        self.layout = layout
        self.width = len(layout[0])
        self.height = len(layout)

        # Calculate the tile size to make the board fill the screen
        self.tile_size = min(screen_width // self.width, screen_height // self.height)

    def draw(self, screen):
        for row_index, row in enumerate(self.layout):
            for col_index, item in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size

                if item == "#":
                    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, self.tile_size, self.tile_size))
                elif item == ".":
                    pygame.draw.circle(screen, (255, 255, 255), (x + self.tile_size // 2, y + self.tile_size // 2),
                                       self.tile_size // 6)
                elif item == "o":
                    pygame.draw.circle(screen, (255, 255, 255), (x + self.tile_size // 2, y + self.tile_size // 2),
                                       self.tile_size // 3)


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