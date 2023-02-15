import pygame

class Button:
    def __init__(self, x, y, image, on_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.on_click = on_click

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.on_click()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
