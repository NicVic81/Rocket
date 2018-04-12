import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, r_settings, screen, rocket):
        """Create a bullet object at the ship's current position."""
        # This properly inherits from Sprite.
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, r_settings.bullet_width, r_settings.bullet_height)
        self.rect.centerx = rocket.rect.centerx
        self.rect.right = rocket.rect.right

        # Store the bullets position as a decimal value like we did earlier for the ship
        # We only need the y value since the bullet will go straight after being shot
        self.x = float(self.rect.x)

        self.color = r_settings.bullet_color
        self.speed_factor = r_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
