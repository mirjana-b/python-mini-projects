import pygame


class Planet:
    def __init__(self, x, y, image, name, on_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.on_click = on_click

        planet_name = name
        font = pygame.font.SysFont(None, 40)
        text_color = (255, 255, 255)

        self.text_offset_x = -18
        self.text_offset_y = 50
        self.planet_name = font.render(planet_name, True, text_color)
        self.hover = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.on_click()

    def is_hovering(self):
        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            self.hover = True
        else:
            self.hover = False

        return self.hover

    def draw(self, screen):
        if not self.is_hovering():
            screen.blit(self.image, (self.rect.x, self.rect.y))
            return

        new_image = pygame.transform.scale(self.image, (200, 200))
        screen_width, _ = screen.get_size()
        text_width, _ = self.planet_name.get_size()
        img_width, _ = new_image.get_size()

        if self.rect.x + self.text_offset_x + text_width + img_width > screen_width:
            text_pos_x = self.rect.x - self.text_offset_x - text_width
            text_pos_y = self.rect.y + self.text_offset_y
        else:
            text_pos_x = self.rect.x + self.text_offset_x + img_width
            text_pos_y = self.rect.y + self.text_offset_y

        screen.blit(new_image, (self.rect.x, self.rect.y))
        screen.blit(self.planet_name, (text_pos_x, text_pos_y))
