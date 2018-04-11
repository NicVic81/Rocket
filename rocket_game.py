import pygame
from r_settings import Settings
from rocket import Rocket
import r_game_functions as rgf


def run_game():
    """Initialize pygame, settings, and screen object."""
    pygame.init()
    rocket_settings = Settings()
    screen = pygame.display.set_mode((rocket_settings.screen_width, rocket_settings.screen_height))
    pygame.display.set_caption("Rocket Man")

    # Make a ship.
    rocket = Rocket(rocket_settings, screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        rgf.check_events(rocket)
        rocket.update()
        # Redraw the screen during each pass through the loop and display the most recent version.
        rgf.update_screen(rocket_settings, screen, rocket)


run_game()
