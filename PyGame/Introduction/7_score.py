import pygame
import os 
import time
import random

scriptDir = os.path.dirname(os.path.realpath(__file__))
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

display_width = 800
display_height = 600
car_width = 64

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load(scriptDir + os.path.sep + 'car.png')

block_color = (53,115,255)

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

# generate objects on screen 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed !')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    # objects creation 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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

        # show objects 
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed


        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()
        
        if thing_starty > display_height:

            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width) 

            dodged += 1
            thing_speed += 0.5
            thing_width += (dodged * 1.2) 

        # if the car and object is same y axis 
        if y < thing_starty + thing_height:
            print('y crossover')
            # check if car is under object x+width and y+height if true its a crash 
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()