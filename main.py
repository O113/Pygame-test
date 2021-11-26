import sys
import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
drawOverview = False;

# Loads grasstile and adds rect
grassTile = pygame.image.load("tile_grass_simple_cross.png")
grassTileRect = grassTile.get_rect()

# Loads dragon and adds rect
dragon = pygame.image.load("dragon_red.png")
dragonTileRect = dragon.get_rect()

# Loads the dragon overview
dragonOverview = pygame.image.load("dragon_overview.png")
dragonOverviewRect = dragonOverview.get_rect()
Rectplace = pygame.draw.rect(screen, (0, 0, 0), (128, 128, 128, 128))

# Loads icon for teeth
teethIcon = pygame.image.load("icon_teeth.png")
teethIconRect = teethIcon.get_rect()


# Draws the grastiles
def drawMap():
    for x in range(20):
        for y in range(15):
            screen.blit(grassTile, [x * 48, y * 48])


# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Update.
        # Mouse position and button clicking.
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        # Check if the rect collided with the mouse pos
        # and if the left mouse button was pressed.
        if Rectplace.collidepoint(pos) and pressed1 and drawOverview is False:
            drawOverview = True;

        if not Rectplace.collidepoint(pos) and pressed1 and drawOverview is True:
            drawOverview = False;

            # Draw.
    drawMap()
    screen.blit(dragon, [128, 128])
    screen.blit(teethIcon, [672,472])
    if drawOverview:
        screen.blit(dragonOverview, dragonOverviewRect)

    fpsClock.tick(fps)
    pygame.display.flip()
