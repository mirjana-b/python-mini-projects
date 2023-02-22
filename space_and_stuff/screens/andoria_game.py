import os
import pygame
import random

from memory_card import Card  # pylint: disable=import-error


class MemoryGame:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        self.background = pygame.image.load(
            os.path.join("pictures", "andoria_planet_background.png"))
        pygame.mixer.music.stop()
        self.background_sound = pygame.mixer.music.load(
            "sounds/andoria_under_the_sea.mp3")
        pygame.mixer.music.play(-1)
        self.calculate_cards_position()
        self.initialize_memory_cards_bg()

    def calculate_cards_position(self):
        self.cards_position = []
        screen_width, screen_height = self.screen.get_size()
        number_of_cards = 16
        num_cards_width = number_of_cards/4
        num_cards_height = number_of_cards/4
        # all images have same size
        card_width, card_height = 150, 150
        card_margin = 10

        x_center = screen_width/2
        y_center = screen_height/2
        cards_width = num_cards_width*card_width + \
            card_margin*(num_cards_width - 1)
        cards_height = num_cards_height*card_height + \
            card_margin*(num_cards_height - 1)
        x_card_start_pos = x_center - cards_width/2
        y_card_start_pos = y_center - cards_height/2

        for i in range(0, number_of_cards):
            x_card = x_card_start_pos + (i % 4)*(card_width + card_margin)
            y_card = y_card_start_pos + (i//4)*(card_height + card_margin)
            self.cards_position.append((x_card, y_card))

    def initialize_memory_card_bg(self, x, y, image_name, name, on_click):
        image = pygame.image.load(os.path.join("pictures", image_name))
        card_bg = Card(x, y, image, name, on_click)
        self.cards_bg.append(card_bg)

    def initialize_memory_cards_bg(self):
        self.cards_bg = []
        random.shuffle(self.cards_position)
        for pos in self.cards_position:
            x_pos, y_pos = pos
            self.initialize_memory_card_bg(x=x_pos, y=y_pos, image_name="at_sea.png",
                                           name="At sea", on_click=self.on_card_clicked)

    # TODO Consider using a function like this instead
    # of having a callback for each card

    def on_something_clicked(self, what):
        pass

    def on_card_clicked(self):
        pass

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))

        for card_bg in self.cards_bg:
            card_bg.draw(self.screen)

        pygame.display.flip()

    def handle_events(self, event):
        pass
