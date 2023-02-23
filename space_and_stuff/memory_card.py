import pygame


class Card:
    def __init__(self, x, y, image_bg, name_bg, image_card, name_card, on_click):
        self.image_bg = image_bg
        self.image_card = image_card
        self.rect = self.image_bg.get_rect()
        self.rect = self.image_card.get_rect()
        self.rect.topleft = (x, y)
        self.card_name_bg = name_bg
        self.card_name = name_card
        self.on_click = on_click

    # TODO Consider reporting what object was clicked
    def whatever(self):
        self.on_click(self)

    def draw(self, screen):
        screen.blit(self.image_card, (self.rect.x, self.rect.y))
