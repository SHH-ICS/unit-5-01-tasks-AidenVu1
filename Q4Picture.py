import pygame

pygame.init()

size = (500, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Smiley Face")

yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (35, 206, 235)

screen.fill(blue)

pygame.draw.circle(screen, yellow, (200, 200), 100)

pygame.draw.circle(screen, red, (150, 150), 20)
pygame.draw.circle(screen, red, (250, 150), 20)

pygame.draw.arc(screen, black, (150, 150, 100, 100), 3.14, 6.28)

pygame.draw.circle(screen, yellow, (80, 220), 20)
pygame.draw.circle(screen, yellow, (320, 220), 20)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

