import pygame
from pygame.sprite import Group
from r_settings import Settings
from rocket import Rocket
import r_game_functions as rgf


def run_game():
    """Initialize pygame, settings, and screen object."""
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode((r_settings.screen_width, r_settings.screen_height))
    pygame.display.set_caption("Rocket Man")

    # Make a ship.
    rocket = Rocket(r_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        rgf.check_events(r_settings, rocket, screen, bullets)
        rocket.update()
        rgf.update_bullets(bullets)
        # Redraw the screen during each pass through the loop and display the most recent version.
        rgf.update_screen(r_settings, screen, rocket, bullets)


run_game()
