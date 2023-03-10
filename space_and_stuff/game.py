import os
import sys
import pygame
from screens.main_menu import MainMenu


class Game():
    def __init__(self):
        pygame.init()  # pylint: disable=no-member
        pygame.mixer.init()

        self.background_sound = pygame.mixer.music.load("./sounds/space.mp3")
        pygame.mixer.music.play(-1)

        self.screen = pygame.display.set_mode(
            (1366, 768), pygame.FULLSCREEN)  # pylint: disable=no-member
        self.background = pygame.image.load(
            os.path.join("./pictures", "space.png"))

        self.screen = MainMenu(self, self.screen)

    def set_screen(self, screen):
        self.screen = screen

    def game_loop(self):
        while True:
            self.screen.update()
            self.screen.render()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pylint: disable=no-member
                    pygame.quit() # pylint: disable=no-member
                    sys.exit()
                else:
                    self.screen.handle_events(event)

            pygame.display.update()


if __name__ == "__main__":
    g = Game()
    g.game_loop()
