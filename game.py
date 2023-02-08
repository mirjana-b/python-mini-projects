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
            (1366, 768), pygame.FULLSCREEN)  # pylint: disable=no-member
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
        andoria_pos_x = 680
        andoria_pos_y = 380
        ardana_pos_x = 466
        ardana_pos_y = 199
        elball_pos_x = 1031
        elball_pos_y = 180
        nibiru_pos_x = 160
        nibiru_pos_y = 90
        omegaIV_pos_x = 487
        omegaIV_pos_y = 640
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
            image=andoria_planet_img)
        self.ardana_planet = Planet(
            x=ardana_pos_x,
            y=ardana_pos_y,
            image=ardana_planet_img)
        self.elball_planet = Planet(
            x=elball_pos_x,
            y=elball_pos_y,
            image=elball_planet_img)
        self.nibiru_planet = Planet(
            x=nibiru_pos_x,
            y=nibiru_pos_y,
            image=nibiru_planet_img)
        self.omegaIV_planet = Planet(
            x=omegaIV_pos_x,
            y=omegaIV_pos_y,
            image=omegaIV_planet_img)
        self.risa_planet = Planet(
            x=risa_pos_x,
            y=risa_pos_y,
            image=risa_planet_img)
        self.vulcan_planet = Planet(
            x=vulcan_pos_x,
            y=vulcan_pos_y,
            image=vulcan_planet_img)
        self.wolf359_planet = Planet(
            x=wolf359_pos_x,
            y=wolf359_pos_y,
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
            self.ardana_planet.draw(self.screen)
            self.elball_planet.draw(self.screen)
            self.nibiru_planet.draw(self.screen)
            self.omegaIV_planet.draw(self.screen)
            self.risa_planet.draw(self.screen)
            self.vulcan_planet.draw(self.screen)
            self.wolf359_planet.draw(self.screen)
        else:
            self.play_button.draw(self.screen)
            self.exit_button.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    g = Game()
    g.game_loop()
