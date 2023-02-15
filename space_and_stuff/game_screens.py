import os
import pygame
import sys
from planet import Planet
from button import Button

#TODO figure out how to separate game states in different files
# (problem with circular import when switching between game states)
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
            image=play_button_img)
        self.exit_button = Button(
            x=width/2 + button_spacing/2,
            y=height/2 - button_height/2,
            image=exit_button_img)

    def update(self):
        pass

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
            pos = pygame.mouse.get_pos()
            if self.exit_button.rect.collidepoint(pos):
                pygame.quit()  # pylint: disable=no-member
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
            pos = pygame.mouse.get_pos()
            if self.play_button.rect.collidepoint(pos):
                self.game.set_screen(GameScreen(self.game, self.screen, self.background))

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.play_button.draw(self.screen)
        self.exit_button.draw(self.screen)

        pygame.display.flip()


class GameScreen:
    def __init__(self,  game, screen, background):
        self.game = game
        self.screen = screen
        self.background = background

        self.initialize_menu_button()
        self.initialize_planets()

    def initialize_menu_button(self):
        menu_button_img = pygame.image.load(
            os.path.join("./pictures", "menu_button.png"))

        menu_pos_x = 36
        menu_pos_y = 20

        self.menu_button = Button(
            x=menu_pos_x,
            y=menu_pos_y,
            image=menu_button_img)

    def initialize_planets(self):
        andoria_pos_x = 680
        andoria_pos_y = 380
        ardana_pos_x = 466
        ardana_pos_y = 199
        elball_pos_x = 1031
        elball_pos_y = 180
        nibiru_pos_x = 160
        nibiru_pos_y = 90
        omegaIV_pos_x = 487
        omegaIV_pos_y = 590
        risa_pos_x = 1200
        risa_pos_y = 500
        vulcan_pos_x = 750
        vulcan_pos_y = 50
        wolf359_pos_x = 145
        wolf359_pos_y = 510

        andoria_planet_img = pygame.image.load(
            os.path.join("./pictures", "andoria.png"))
        ardana_planet_img = pygame.image.load(
            os.path.join("./pictures", "ardana.png"))
        elball_planet_img = pygame.image.load(
            os.path.join("./pictures", "elball.png"))
        nibiru_planet_img = pygame.image.load(
            os.path.join("./pictures", "nibiru.png"))
        omegaIV_planet_img = pygame.image.load(
            os.path.join("./pictures", "omegaIV.png"))
        risa_planet_img = pygame.image.load(
            os.path.join("./pictures", "risa.png"))
        vulcan_planet_img = pygame.image.load(
            os.path.join("./pictures", "vulcan.png"))
        wolf359_planet_img = pygame.image.load(
            os.path.join("./pictures", "wolf359.png"))

        self.andoria_planet = Planet(
            x=andoria_pos_x,
            y=andoria_pos_y,
            image=andoria_planet_img,
            name="Andoria")
        self.ardana_planet = Planet(
            x=ardana_pos_x,
            y=ardana_pos_y,
            image=ardana_planet_img,
            name="Ardana")
        self.elball_planet = Planet(
            x=elball_pos_x,
            y=elball_pos_y,
            image=elball_planet_img,
            name="Elball")
        self.nibiru_planet = Planet(
            x=nibiru_pos_x,
            y=nibiru_pos_y,
            image=nibiru_planet_img,
            name="Nibiru")
        self.omegaIV_planet = Planet(
            x=omegaIV_pos_x,
            y=omegaIV_pos_y,
            image=omegaIV_planet_img,
            name="OmegaIV")
        self.risa_planet = Planet(
            x=risa_pos_x,
            y=risa_pos_y,
            image=risa_planet_img,
            name="Risa")
        self.vulcan_planet = Planet(
            x=vulcan_pos_x,
            y=vulcan_pos_y,
            image=vulcan_planet_img,
            name="Vulcan")
        self.wolf359_planet = Planet(
            x=wolf359_pos_x,
            y=wolf359_pos_y,
            image=wolf359_planet_img,
            name="Wolf359")

    def update(self):
        pass

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
            pos = pygame.mouse.get_pos()
            if self.menu_button.rect.collidepoint(pos):
                self.game.set_screen(MainMenu(self.game, self.screen, self.background))

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.andoria_planet.draw(self.screen)
        self.ardana_planet.draw(self.screen)
        self.elball_planet.draw(self.screen)
        self.nibiru_planet.draw(self.screen)
        self.omegaIV_planet.draw(self.screen)
        self.risa_planet.draw(self.screen)
        self.vulcan_planet.draw(self.screen)
        self.wolf359_planet.draw(self.screen)
        self.menu_button.draw(self.screen)

        pygame.display.flip()
