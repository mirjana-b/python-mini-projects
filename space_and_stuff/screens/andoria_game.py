import os
import pygame
import random

from memory_card import Card  # pylint: disable=import-error
from screens import game_screen  # pylint: disable=import-error
from button import Button  # pylint: disable=import-error


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
        self.initialize_memory_cards()
        self.initialize_back_button()

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

    def initialize_memory_card(self, x, y, image_bg_name, name_bg, image_card, name_card, on_click):
        image_bg = pygame.image.load(os.path.join("pictures", image_bg_name))
        image = pygame.image.load(os.path.join("pictures", image_card))
        card = Card(x, y, image_bg, name_bg, image, name_card, on_click)
        self.cards.append(card)

    def initialize_memory_cards(self):
        self.cards = []
        random.shuffle(self.cards_position)

        card_images = ["octopus.png", "sea_turtle.png", "giant_squid.png", "seahorse.png", "dolphin.png", "mermaid.png", "sea_dragon.png", "angler_fish.png",
                       "octopus.png", "sea_turtle.png", "giant_squid.png", "seahorse.png", "dolphin.png", "mermaid.png", "sea_dragon.png", "angler_fish.png"]
        card_names = ["Octopus", "Sea Turtle", "Giant Squid", "Seahorse", "Dolphin", "Mermaid", "Sea Dragon", "Angler Fish",
                      "Octopus", "Sea Turtle", "Giant Squid", "Seahorse", "Dolphin", "Mermaid", "Sea Dragon", "Angler Fish",]

        for i, pos in enumerate(self.cards_position):
            x_pos, y_pos = pos
            self.initialize_memory_card(x=x_pos, y=y_pos, image_bg_name="at_sea.png",
                                        name_bg="At sea", image_card=card_images[i], name_card=card_names[i], on_click=self.on_card_clicked)

    def initialize_back_button(self):
        back_button_img = pygame.image.load(
            os.path.join("pictures", "back.png"))

        back_pos_x = 36
        back_pos_y = 20

        self.back_button = Button(
            x=back_pos_x,
            y=back_pos_y,
            image=back_button_img,
            on_click=self.on_back_clicked)

    def on_back_clicked(self):
        self.game.set_screen(game_screen.GameScreen(
            self.game, self.screen))

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
        self.back_button.draw(self.screen)

        for card in self.cards:
            card.draw(self.screen)

        pygame.display.flip()

    def handle_events(self, event):
        self.back_button.handle_event(event)
