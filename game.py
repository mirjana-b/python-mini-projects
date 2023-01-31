import time
import os
import pygame

class Game():
    def __init__(self):
        pygame.init()# pylint: disable=no-member
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)# pylint: disable=no-member
        self.background = pygame.image.load(os.path.join("./pictures", "space.png"))
        self.running = True
        self.d_time, self.prev_time = 0, 0

    def game_loop(self):
        while self.running:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pylint: disable=no-member
                self.running = False
        #TODO implement more events after I decide what will be my game logic

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.d_time = now - self.prev_time
        self.prev_time = now


if __name__ == "__main__":
    g = Game()
    g.game_loop()