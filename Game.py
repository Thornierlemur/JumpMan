import pygame
import sys

#used to save and load the game
import pickle

# Setup pygame/window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('JumpMan')

# screen resolution
res = (600, 400)
screen = pygame.display.set_mode(res, 0, 32)

# Fonts used
font = pygame.font.SysFont(None, 20)
button_font = pygame.font.SysFont(None, 50)

# Colors
black = (0,0,0)

# click variable to detect when the user clicks a button
click = False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:

        screen.fill(black)
        draw_text('main menu', font, (255, 255,255), screen, 20, 20)

        # gets the x and y positions of the mouse and puts them
        # into our variables mx, my
        mx, my = pygame.mouse.get_pos()

        # Creation of our buttons
        # x, y, length, height
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 220, 50)
        button_4 = pygame.Rect(300, 100, 260, 50)
        button_5 = pygame.Rect(300, 200, 200, 50)

        # checking for collisions
        if button_1.collidepoint((mx, my)):
            if click:
                level1()
        if button_2.collidepoint((mx, my)):
            if click:
                LoadGame()
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
        draw_text("LeaderBoards", button_font, (0,0,0), screen, 300, 100)

        pygame.draw.rect(screen, (255,255,255), button_5)
        draw_text("Exit", button_font, (0,0,0), screen, 300, 200)

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


def exit():
    pygame.quit()
    sys.exit()

def LevelSelect():
    pygame.quit()
    sys.exit()

# this function allows for me to save a game while playing
def SaveGame():
    with open("savegame", "wb") as f:
        pickle.dump(foo, f)

# This function allows for me to load a game
def LoadGame():
    with open("savegame", "rb") as f:
        foo = pickle.load(f)

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)

    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

def level1():
    screen.fill(black)

    # like an image! (resolution)
    display = pygame.Surface((300, 200))

    game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
                ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

    # Get the player image
    # Note a path can be created to the player images!
    # example path 'images/king.png'
    player_image = pygame.image.load('player.png')
    player_image.set_colorkey((255, 255, 255))

    grass_image = pygame.image.load('grass.png')
    TILE_SIZE = grass_image.get_width()

    dirt_image = pygame.image.load('dirt.png')

    # This is for just right now
    draw_text('game', font, (255, 255,255), screen, 20, 20)

    # Player movement variables
    moving_right = False
    moving_left = False
    player_y_momentum = 0
    air_timer = 0

    # Collision!
    player_rect = pygame.Rect(50, 50, player_image.get_width(), player_image.get_height())
    test_rect = pygame.Rect(100, 100, 100, 50)
    # x, y, wide, tall ^

    running = True
    while running:
        # red, green, blue
        display.fill((146,244,255))

        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile == '1':
                    display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
                if tile == '2':
                    display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                x += 1
            y += 1

        #Player movement
        player_movement = [0, 0]
        if moving_right:
            player_movement[0] += 2
        if moving_left:
            player_movement[0] -= 2
        player_movement[1] += player_y_momentum
        player_y_momentum += 0.2

        if player_y_momentum > 3:
            player_y_momentum = 3
        
        player_rect, collisions = move(player_rect, player_movement, tile_rects)
        
        if collisions['bottom']:
            player_y_momentum = 0
            air_timer = 0
        else:
            air_timer += 1

        # render the player image onto the screen
        # (50,50) -> x, y (these values are inverted)
        display.blit(player_image, (player_rect.x, player_rect.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    if air_timer < 6:
                        player_y_momentum = -5
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False
        
        # changes the size of my smaller image to be the size
        # of the new image
        surf = pygame.transform.scale(display, res)
        screen.blit(surf, (0, 0))

        pygame.display.update()
        mainClock.tick(60) 

main_menu()


##class Game:
    