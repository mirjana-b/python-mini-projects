import os
import pygame


class MemoryGame:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        self.background = pygame.image.load(
            os.path.join("pictures", "andoria_planet_background.png"))
        pygame.mixer.music.stop()
        self.background_sound = pygame.mixer.music.load("sounds/andoria_under_the_sea.mp3")
        pygame.mixer.music.play(-1)

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def handle_events(self, event):
        pass