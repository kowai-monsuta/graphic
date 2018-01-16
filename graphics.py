import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
RED = (242, 62, 16)
GREY = (56, 67, 86)
BLUEE = (115, 99, 237)
BLACK = (0,0,0)
YELLOWW = (250, 255, 0)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def draw_line():
    y = 240
    for y in range(240,500,10):
        pygame.draw.line(screen, WHITE, [400, y + 10], [700, y + 10], 2)
    
def draw_window(x,y):
    pygame.draw.rect(screen, YELLOWW, [x + 20, y + 20,60,70])
    
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    
             
    # Drawing code
    ''' sky '''
    screen.fill(BLUE)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [175, 75, 100, 100])

    ''' clouds '''
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)
    draw_cloud(575, 70)

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    pygame.draw.ellipse(screen, GREY, [57,427,307,157])
    pygame.draw.ellipse(screen, BLUEE, [60,430,300,150])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' house '''
    pygame.draw.rect(screen, RED, [400, 250, 300, 250])
    pygame.draw.rect(screen, WHITE, [530, 440, 40, 60])
    draw_line()
    draw_window(430,270)
    draw_window(570,270)
    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()
