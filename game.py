import time
import os
import pygame
from button import Button

class Game():
    def __init__(self):
        pygame.init()# pylint: disable=no-member
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)# pylint: disable=no-member
        self.background = pygame.image.load(os.path.join("./pictures", "space.png"))
        self.running = True
        self.w, self.h = pygame.display.get_surface().get_size()
        self.play_button_img = pygame.image.load(os.path.join("./pictures", "play_button.png"))
        self.exit_button_img = pygame.image.load(os.path.join("./pictures", "exit_button.png"))
        self.play_button = Button(self.w/2 - 275 - 10, self.h/2 - 70, self.play_button_img)
        self.exit_button = Button(self.w/2 + 10, self.h/2 - 70, self.exit_button_img)

    def game_loop(self):
        while self.running:
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                self.running = False

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.play_button.draw(self.screen)
        self.exit_button.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    g = Game()
    g.game_loop()