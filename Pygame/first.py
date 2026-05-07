#24.09
import pygame
import os

width, height = 900, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello World!")
bkgcolor = (20, 30, 155)
fps = 60

pink = pygame.image.load(os.path.join('Pygame', 'IMGS', 'PShip.png'))
green = pygame.image.load(os.path.join('Pygame', 'IMGS', 'GShip.png'))

#newPink = 
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                run = False
        drawing()
    pygame.quit()

def drawing():
#order matters
    win.fill(bkgcolor)
    win.blit(pink, (50, 50))
    win.blit(green, (100, 100)) #surface on screen
    pygame.display.update()

if __name__ == "__main__":
    main()