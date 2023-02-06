import os
import pygame
from button import Button
from planet import Planet


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
        self.playing = False
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

        self.initialize_planets()

    def initialize_planets(self):
        width, height = pygame.display.get_surface().get_size()

        andoria_planet_img = pygame.image.load(
            os.path.join("./pictures", "andoria.png"))
        ardana_planet_img = pygame.image.load(
            os.path.join("./pictures", "ardana.png"))
        elball_planet_img = pygame.image.load(
            os.path.join("./pictures", "elball.png"))
        nibiru_planet_img = pygame.image.load(
            os.path.join("./pictures", "nibiru.png"))
        omegaIV_planet_img = pygame.image.load(
            os.path.join("./pictures", "risa.png"))
        risa_planet_img = pygame.image.load(
            os.path.join("./pictures", "risa.png"))
        vulcan_planet_img = pygame.image.load(
            os.path.join("./pictures", "vulcan.png"))
        wolf359_planet_img = pygame.image.load(
            os.path.join("./pictures", "wolf359.png"))

        self.andoria_planet = Planet(
            x=width/2,
            y=height/2,
            image=andoria_planet_img)
        self.ardana_planet = Planet(
            x=width/2,
            y=height/2,
            image=ardana_planet_img)
        self.elball_planet = Planet(
            x=width/2,
            y=height/2,
            image=elball_planet_img)
        self.nibiru_planet = Planet(
            x=width/2,
            y=height/2,
            image=nibiru_planet_img)
        self.omegaIV_planet = Planet(
            x=width/2,
            y=height/2,
            image=omegaIV_planet_img)
        self.risa_planet = Planet(
            x=width/2,
            y=height/2,
            image=risa_planet_img)
        self.vulcan_planet = Planet(
            x=width/2,
            y=height/2,
            image=vulcan_planet_img)
        self.wolf359_planet = Planet(
            x=width/2,
            y=height/2,
            image=wolf359_planet_img)

    def game_loop(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=no-member
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:# pylint: disable=no-member
                pos = pygame.mouse.get_pos()
                if self.exit_button.rect.collidepoint(pos) and self.playing == False:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:# pylint: disable=no-member
                pos = pygame.mouse.get_pos()
                if self.play_button.rect.collidepoint(pos):
                    self.playing = True


    def update(self):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))

        if self.playing:
            self.andoria_planet.draw(self.screen)
        else:
            self.play_button.draw(self.screen)
            self.exit_button.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    g = Game()
    g.game_loop()
