import pygame, sys

pygame.init()

display = pygame.display.set_mode((600, 300))

pygame.display.set_caption("My Game")

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

rect = pygame.Rect(60, 30, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    display.fill((30, 30, 30))
    pygame.draw.rect(display, (200, 200, 200), rect)
    pygame.display.update()