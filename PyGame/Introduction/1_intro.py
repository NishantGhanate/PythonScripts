import pygame

# Initiliase game package
pygame.init()

# Set game window resolution
gameDisplay = pygame.display.set_mode((800,600))
# Set game window title
pygame.display.set_caption('A bit Racey')
# set clock
clock = pygame.time.Clock()

crashed = False

while not crashed:
    # game event listener
    for event in pygame.event.get():

        # if window closed exit the game
        if event.type == pygame.QUIT:
            crashed = True

        # print the event type keyboad mouse
        print(event)

    # update the screen  its 30fps
    pygame.display.update()
    
    # start clock 60seconds
    clock.tick(60)

# terminate
pygame.quit()
quit()