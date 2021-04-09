import pygame
import sys
import os
import random

#used to save and load the game
import pickle

# Setup pygame/window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('JumpMan')

# Sound initialization
pygame.mixer.pre_init(44100, -16, 2, 512)

# screen resolution
res = (600, 400)
screen = pygame.display.set_mode(res, 0, 32)

# Fonts used
font = pygame.font.SysFont(None, 20)
button_font = pygame.font.SysFont(None, 50)

# Colors
black = (0,0,0)
Baby_Blue = (146,244,255)
white = (255,255,255)

# click variable to detect when the user clicks a button
click = False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

def main_menu():
    while True:

        screen.fill(Baby_Blue)
        draw_text('main menu', font, black, screen, 20, 20)

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

global animation_frames
animation_frames = {}

def load_animation(path, frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        animation_image = pygame.image.load(img_loc).convert()
        animation_image.set_colorkey(white)
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var,frame

def level1():
    screen.fill(black)

    # like an image! (resolution)
    display = pygame.Surface((300, 200))

    animation_database = {}
    animation_database['run'] = load_animation('player_animations/run', [7,7])
    animation_database['idle'] = load_animation('player_animations/idle', [7,7,40])

    player_action = 'idle'
    player_frame = 0
    player_flip = False

    # Loading the map
    game_map = load_map('map')

    grass_image = pygame.image.load('images/grass.png')
    TILE_SIZE = grass_image.get_width()
    dirt_image = pygame.image.load('images/dirt.png')

    # Sounds
    jump_sound = pygame.mixer.Sound('audio/jump.wav')
    grass_sounds = [pygame.mixer.Sound('audio/grass_0.wav'),pygame.mixer.Sound('audio/grass_1.wav')]
    grass_sounds[0].set_volume(0.2)
    grass_sounds[1].set_volume(0.2)
    pygame.mixer.music.load('audio/music.wav')
    pygame.mixer.music.play(-1)
    grass_sound_timer = 0

    # This is for just right now
    draw_text('game', font, (255, 255,255), screen, 20, 20)

    # [scroll value, [x, y, width, height]]
    background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]

    # Player movement variables
    moving_right = False
    moving_left = False
    player_y_momentum = 0
    air_timer = 0
    true_scroll = [0,0]

    # Collision!
    player_rect = pygame.Rect(100,100,5,13)

    running = True
    while running:
        # red, green, blue
        display.fill((146,244,255))

        if grass_sound_timer > 0:
            grass_sound_timer -= 1

        # Camera following player
        true_scroll[0] += (player_rect.x - true_scroll[0] - 152)/20
        true_scroll[1] += (player_rect.y - true_scroll[1] - 106)/20

        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        # Dark Green
        pygame.draw.rect(display, (7, 80, 75), pygame.Rect(0,120,300,80))
        for background_object in background_objects:
            obj_rect = pygame.Rect(background_object[1][0] - scroll[0]*background_object[0], background_object[1][1] - scroll[1]*background_object[0], background_object[1][2], background_object[1][3])
            if background_object[0] == 0.5:
                pygame.draw.rect(display, (14, 222,150),obj_rect) # rendering the object a certain value based on its scroll multiplier
            else:
                pygame.draw.rect(display, (9, 91, 85),obj_rect)

        #scroll[0] += 1 This allows for the camera to continuously move to the right

        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile == '1':
                    display.blit(dirt_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                if tile == '2':
                    display.blit(grass_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
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
        
        # Player runs to the right
        if player_movement[0] > 0:
            player_action,player_frame = change_action(player_action,player_frame,'run')
            player_flip = False
        # Player is not moving, make animation idle
        if player_movement[0] == 0:
            player_action,player_frame = change_action(player_action,player_frame,'idle')
        # Player runs to the left
        if player_movement[0] < 0:
            player_action,player_frame = change_action(player_action,player_frame,'run')
            player_flip = True
        
        player_rect, collisions = move(player_rect, player_movement, tile_rects)
        
        if collisions['bottom'] == True:
            player_y_momentum = 0
            air_timer = 0
            if player_movement[0] != 0:
                if grass_sound_timer == 0:
                    grass_sound_timer = 30
                    random.choice(grass_sounds).play()
        else:
            air_timer += 1


        player_frame += 1
        # if the frame has passed the amount of frames available
        if player_frame >= len(animation_database[player_action]):
            player_frame = 0
        player_img_id = animation_database[player_action][player_frame]
        player_img = animation_frames[player_img_id]
        # render the player image onto the screen
        # (50,50) -> x, y (these values are inverted)
        display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    pygame.mixer.music.fadeout(1000)
                if event.key == K_e:
                    pygame.mixer.music.play(-1)
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    if air_timer < 6:
                        jump_sound.play()
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
    pygame.mixer.music.fadeout(500)

main_menu()


##class Game:
    