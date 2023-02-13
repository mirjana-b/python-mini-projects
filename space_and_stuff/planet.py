import pygame


class Planet:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.hover = False


    def is_hovering(self):
        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            self.hover = True
        else:
            self.hover= False

        return self.hover

    def draw(self, screen):
        if self.is_hovering():
            new_image = pygame.transform.scale(self.image, (200, 200))
            screen.blit(new_image, (self.rect.x, self.rect.y))
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))