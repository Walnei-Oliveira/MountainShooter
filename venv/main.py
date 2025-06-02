import pygame

print('Setup Start')
# starting Pygame
pygame.init()

# setting window size
screen = pygame.display.set_mode(size=(600, 480))
pygame.display.set_caption("Montain Shooter Game")

print('Loop Start')
# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # setting screen background color (RGB: white blue)
    screen.fill((135, 206, 235))
    pygame.display.flip()

# ending Pygame
print('End')
pygame.quit()
