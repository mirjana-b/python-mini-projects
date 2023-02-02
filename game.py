import os
import pygame
from button import Button


class Game():
    def __init__(self):
        pygame.init()  # pylint: disable=no-member
        pygame.mixer.init()

        self.background_sound = pygame.mixer.music.load("./sounds/space.mp3")
        pygame.mixer.music.play(-1)

        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)  # pylint: disable=no-member
        self.background = pygame.image.load(
            os.path.join("./pictures", "space.png"))

        self.running = True
        width, height = pygame.display.get_surface().get_size()

        play_button_img = pygame.image.load(
            os.path.join("./pictures", "play_button.png"))
        exit_button_img = pygame.image.load(
            os.path.join("./pictures", "exit_button.png"))

        # Both buttons have the same size
        button_width = play_button_img.get_width()
        button_height = play_button_img.get_height()
        button_spacing = 20

        self.play_button = Button(
            x=width/2 - button_width - button_spacing/2,
            y=height/2 - button_height/2,
            image=play_button_img)
        self.exit_button = Button(
            x=width/2 + button_spacing/2,
            y=height/2 - button_height/2,
            image=exit_button_img)

    def game_loop(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=no-member
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
