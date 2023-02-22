import pygame


class Card:
    def __init__(self, x, y, image, name, on_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.card_name = name
        self.on_click = on_click

    # TODO Consider reporting what object was clicked
    def whatever(self):
        self.on_click(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
