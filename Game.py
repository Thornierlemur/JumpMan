import pygame 
import sys

# Setup pygame/window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('base case')

# screen resolution
res = (720, 720)
screen = pygame.display.set_mode(res)

font = pygame.font.SysFont(None, 20)
button_font = pygame.font.SysFont(None, 50)

# click variable to detect when the user clicks a button
click = False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:

        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255,255), screen, 20, 20)

        # gets the x and y positions of the mouse and puts them
        # into our variables mx, my
        mx, my = pygame.mouse.get_pos()

        # Creation of our buttons
        # x, y, length, height
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 220, 50)
        button_4 = pygame.Rect(50, 400, 260, 50)
        button_5 = pygame.Rect(50, 500, 200, 50)

        # checking for collisions
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                Load()
        if button_3.collidepoint((mx, my)):
            if click:
                LevelSelect()
        if button_4.collidepoint((mx, my)):
            if click:
                game()
        if button_5.collidepoint((mx, my)):
            if click:
                exit()

        # renders the buttons
        pygame.draw.rect(screen, (255,255,255), button_1)
        draw_text("New Game", button_font, (0,0,0), screen, 50, 100)

        pygame.draw.rect(screen, (255,255,255), button_2)
        draw_text("Load", button_font, (0,0,0), screen, 50, 200)

        pygame.draw.rect(screen, (255,255,255), button_3)
        draw_text("Level Select", button_font, (0,0,0), screen, 50, 300)

        pygame.draw.rect(screen, (255,255,255), button_4)
        draw_text("LeaderBoards", button_font, (0,0,0), screen, 50, 400)

        pygame.draw.rect(screen, (255,255,255), button_5)
        draw_text("Exit", button_font, (0,0,0), screen, 50, 500)

        # must reset the click variable before every event
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # case when the user clicks onto a button
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
            pygame.display.update()
            mainClock.tick(60) # framerate of the game

def game():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('game', font, (255, 255,255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # if the user presses the 'esc' key the function ends
                # and returns to wherever the function called it
                if event.key == K_ESCAPE:
                    running = False
            
            pygame.display.update()
            mainClock.tick(60) 


def Load():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Load menu', font, (255, 255,255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # if the user presses the 'esc' key the function ends
                # and returns to wherever the function called it
                if event.key == K_ESCAPE:
                    running = False
            
            pygame.display.update()
            mainClock.tick(60) 

def exit():
    pygame.quit()
    sys.exit()

def LevelSelect():
    pygame.quit()
    sys.exit()

main_menu()


##class Game:
    