import os
import sys
import pygame

#TODO solve why pylint shows import-error(import works)
from screens import game_screen # pylint: disable=import-error
from button import Button # pylint: disable=import-error

class MainMenu:
    def __init__(self,  game, screen, background):
        self.game = game
        self.screen = screen
        self.background = background

        self.initialize_buttons()

    def initialize_buttons(self):
        width, height = pygame.display.get_surface().get_size()

        play_button_img = pygame.image.load(
            os.path.join("./pictures", "play_button.png"))
        exit_button_img = pygame.image.load(
            os.path.join("./pictures", "exit_button.png"))

        # Both(play and exit) buttons have the same size
        button_width = play_button_img.get_width()
        button_height = play_button_img.get_height()
        button_spacing = 20

        self.play_button = Button(
            x=width/2 - button_width - button_spacing/2,
            y=height/2 - button_height/2,
            image=play_button_img,
            on_click=self.on_play_clicked)
        self.exit_button = Button(
            x=width/2 + button_spacing/2,
            y=height/2 - button_height/2,
            image=exit_button_img,
            on_click=self.on_exit_clicked)

    def on_exit_clicked(self):
        pygame.quit()  # pylint: disable=no-member
        sys.exit()

    def on_play_clicked(self):
        self.game.set_screen(game_screen.GameScreen(self.game, self.screen, self.background))

    def update(self):
        pass

    def handle_events(self, event):
        self.exit_button.handle_event(event)
        self.play_button.handle_event(event)

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.play_button.draw(self.screen)
        self.exit_button.draw(self.screen)

        pygame.display.flip()
