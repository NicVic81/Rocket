import pygame


class Rocket:

    def __init__(self, r_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.r_settings = r_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocketsideways.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the center of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ship's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ships position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.r_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.r_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.centery -= self.r_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.r_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
