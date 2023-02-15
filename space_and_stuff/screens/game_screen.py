import os
import pygame
from screens import main_menu
from planet import Planet
from button import Button


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

    def initialize_planet(self, x, y, image_name, name):
        image = pygame.image.load(os.path.join("./pictures", image_name))
        planet = Planet(x, y, image, name)
        self.planets.append(planet)

    def initialize_planets(self):
        self.planets = []

        self.initialize_planet(x=680, y=380, image_name="andoria.png", name="Andoria")
        self.initialize_planet(x=466, y=199, image_name="ardana.png", name="Ardana")
        self.initialize_planet(x=1031, y=180, image_name="elball.png", name="Elball")
        self.initialize_planet(x=160, y=90, image_name="nibiru.png", name="Nibiru")
        self.initialize_planet(x=487, y=590, image_name="omegaIV.png", name="OmegaIV")
        self.initialize_planet(x=1200, y=500, image_name="risa.png", name="Risa")
        self.initialize_planet(x=750, y=50, image_name="vulcan.png", name="Vulcan")
        self.initialize_planet(x=145, y=510, image_name="wolf359.png", name="Wolf359")

    def update(self):
        pass

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
            pos = pygame.mouse.get_pos()
            if self.menu_button.rect.collidepoint(pos):
                self.game.set_screen(main_menu.MainMenu(self.game, self.screen, self.background))

    def render(self):
        self.screen.blit(self.background, (0, 0))

        for planet in self.planets:
            planet.draw(self.screen)

        self.menu_button.draw(self.screen)

        pygame.display.flip()
