import os
import pygame

# TODO solve why pylint shows import-error(import works)
from screens import main_menu, andoria_game  # pylint: disable=import-error
from planet import Planet  # pylint: disable=import-error
from button import Button  # pylint: disable=import-error


class GameScreen:
    def __init__(self,  game, screen):
        self.background_sound = pygame.mixer.music.load("./sounds/space.mp3")
        pygame.mixer.music.play(-1)
        self.background = pygame.image.load(
            os.path.join("./pictures", "space.png"))
        self.game = game
        self.screen = screen

        self.initialize_menu_button()
        self.initialize_planets()

    def initialize_menu_button(self):
        menu_button_img = pygame.image.load(
            os.path.join("./pictures", "menu.png"))

        menu_pos_x = 36
        menu_pos_y = 20

        self.menu_button = Button(
            x=menu_pos_x,
            y=menu_pos_y,
            image=menu_button_img,
            on_click=self.on_menu_clicked)

    def initialize_planet(self, x, y, image_name, name, on_click):
        image = pygame.image.load(os.path.join("./pictures", image_name))
        planet = Planet(x, y, image, name, on_click)
        self.planets.append(planet)

    def initialize_planets(self):
        self.planets = []

        self.initialize_planet(x=680, y=380, image_name="andoria.png",
                               name="Andoria", on_click=self.on_andoria_clicked)
        self.initialize_planet(x=466, y=199, image_name="ardana.png",
                               name="Ardana", on_click=self.on_ardana_clicked)
        self.initialize_planet(x=1031, y=180, image_name="elball.png",
                               name="Elball", on_click=self.on_elball_clicked)
        self.initialize_planet(x=160, y=90, image_name="nibiru.png",
                               name="Nibiru", on_click=self.on_nibiru_clicked)
        self.initialize_planet(x=487, y=590, image_name="omegaIV.png",
                               name="OmegaIV", on_click=self.on_omegaIV_clicked)
        self.initialize_planet(
            x=1200, y=500, image_name="risa.png", name="Risa", on_click=self.on_risa_clicked)
        self.initialize_planet(x=750, y=50, image_name="vulcan.png",
                               name="Vulcan", on_click=self.on_vulcan_clicked)
        self.initialize_planet(x=145, y=510, image_name="wolf359.png",
                               name="Wolf359", on_click=self.on_wolf359_clicked)

    def update(self):
        pass

    def on_menu_clicked(self):
        self.game.set_screen(main_menu.MainMenu(
            self.game, self.screen))

    def on_andoria_clicked(self):
        self.game.set_screen(andoria_game.MemoryGame(
            self.game, self.screen))

    def on_ardana_clicked(self):
        pass

    def on_elball_clicked(self):
        pass

    def on_nibiru_clicked(self):
        pass

    def on_omegaIV_clicked(self):
        pass

    def on_risa_clicked(self):
        pass

    def on_vulcan_clicked(self):
        pass

    def on_wolf359_clicked(self):
        pass

    def handle_events(self, event):
        self.menu_button.handle_event(event)

        for planet in self.planets:
            planet.handle_event(event)

    def render(self):
        self.screen.blit(self.background, (0, 0))

        for planet in self.planets:
            planet.draw(self.screen)

        self.menu_button.draw(self.screen)

        pygame.display.flip()
