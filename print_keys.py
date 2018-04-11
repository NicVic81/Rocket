import sys
import pygame


def run_key():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Key Capture")
    pygame.font.init()

    # Start the main loop


    while True:

    # Watch for keyboard and mouse events.
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                key_code = str(event.key)
                text_surface = my_font.render(key_code, False, (255, 255, 255))
                screen.fill((0, 0, 0,))
                screen.blit(text_surface,(0,0))

        pygame.display.flip()

run_key()
