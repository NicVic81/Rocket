import sys
import pygame
from bullet import Bullet

def check_events(r_settings, screen, rocket, bullets):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, r_settings, screen, rocket, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def check_keydown_events(event, r_settings, screen, rocket, bullets):
    """Respond to key down key presses"""
    if event.key == pygame.K_RIGHT:
        # Move the hip to the right
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        # Move the ship up.
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move the ship down
        rocket.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(r_settings, screen, rocket, bullets)


def check_keyup_events(event, rocket):
    """Respond to key up key presses"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def fire_bullets(r_settings, screen, rocket, bullets):
    # Create a bullet and add it to the bullet group if there is less than the max number of bullets on screen
    if len(bullets) < r_settings.bullets_allowed:
        new_bullet = Bullet(r_settings, screen, rocket)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet position
    bullets.update()

    # Get rid of bullets that have disapperared.
    for bullet in bullets.copy():
        if bullet.rect.left >= 800:
            bullets.remove(bullet)

def update_screen(r_settings, screen, rocket, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(r_settings.bg_color)
    # Redraw all the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
