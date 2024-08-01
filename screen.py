import pygame
import sys


def start_screen(screen):
    black = (0, 0, 0)
    white = (255, 255, 255)

    font = pygame.font.Font(None, 77)
    smaller_font = pygame.font.Font(None, 36)

    title_text = font.render("Pac-Man", True, white)
    start_text = smaller_font.render("Press any key to start", True, white)

    screen_width, screen_height = screen.get_size()
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    start_rect = start_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

        screen.fill(black)
        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)
        pygame.display.flip()
