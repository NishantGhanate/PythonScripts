import pygame
import os 

scriptDir = os.path.dirname(os.path.realpath(__file__))
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 64

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load(scriptDir + os.path.sep + 'car.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x,y)
        
        # if the car touches boundry 
        if x > display_width - car_width or x < 0:
            gameExit = True
            
        
        pygame.display.update()
        clock.tick(60)



game_loop()
pygame.quit()
quit()