import pygame, sys, os, random
from pygame.locals import *
import os.path
from os import path
import random
import pygame.freetype

# Setup pygame/window
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('JumpMan')

# Sound initialization
pygame.mixer.pre_init(44100, -16, 2, 512)

# screen resolution
res = (800, 600)
screen = pygame.display.set_mode(res, 0, 32)

# Fonts used
font = pygame.font.SysFont(None, 20)
font2 = pygame.font.SysFont(None, 30)
button_font = pygame.font.Font("fonts/ka1.ttf", 30)
title_font = pygame.font.Font("fonts/ka1.ttf", 50)

# Load image used for login background, can be any image
my_image = pygame.image.load('images/image2.png')
ldr_image = pygame.image.load('images/image2.jpg')

# Colors
black = (0,0,0)
Baby_Blue = (146,244,255)
white = (255,255,255)

# Mute Bool
global Mute 
Mute = False

# Intent: Helper function that helps the programmer draw text
#         to the screen.
# Preconditions: All variables are passed legal data
#                when the function is called
# Postcondition: Draws text onto the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Intent: Helper function to load the map.txt file into the game
# Precondition: path is always given a .txt file named map(integer value here)
# Postcondition: The Function returns the map of the level in a 2d array format
def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

# Intent: The user is shown the main menu of the game
# Precondition: username = a legal username that is given from
#               the login window when the user logs into their account
def main_menu(username):
    # click variable to detect when the user clicks a button
    click = False
    while True:

        #screen.fill(Baby_Blue)
        # To change background from a color to image
        screen.blit(my_image, (0, 0))
        draw_text('main menu', font, black, screen, 20, 20)
        draw_text('JumpMan', title_font, black, screen, 250, 20)

        # gets the x and y positions of the mouse and puts them
        # into our variables mx, my
        mx, my = pygame.mouse.get_pos()

        # Creation of our buttons
        # x, y, length, height
        button_1 = pygame.Rect(50, 100, 200, 40) # old 50,100,200,50
        button_2 = pygame.Rect(50, 200, 100, 40) # old 50,200,200,50
        button_3 = pygame.Rect(50, 300, 280, 40) # old 50,300,220,50
        button_4 = pygame.Rect(50, 400, 310, 40) # old 300,100,260,50
        button_5 = pygame.Rect(50, 500, 100, 40) # old 300,200,200,50

        # checking for collisions
        if button_1.collidepoint((mx, my)):
            if click:
                location = [0,0]
                level1(location, username, '1')
        if button_2.collidepoint((mx, my)):
            if click:
                LoadGame(username)
        if button_3.collidepoint((mx, my)):
            if click:
                LevelSelect(username)
        if button_4.collidepoint((mx, my)):
            if click:
                LeaderBoards()
        if button_5.collidepoint((mx, my)):
            if click:
                Exit()

        # renders the buttons

        #pygame.draw.rect(screen, (255,255,255), button_1)
        draw_text("New Game", button_font, (0,0,0), screen, 50, 100)

        #pygame.draw.rect(screen, (255,255,255), button_2)
        draw_text("Load", button_font, (0,0,0), screen, 50, 200)

        #pygame.draw.rect(screen, (255,255,255), button_3)
        draw_text("Level Select", button_font, (0,0,0), screen, 50, 300)

        #pygame.draw.rect(screen, (255,255,255), button_4)
        draw_text("LeaderBoards", button_font, (0,0,0), screen, 50, 400) # old 300,100

        #pygame.draw.rect(screen, (255,255,255), button_5)
        draw_text("Exit", button_font, (0,0,0), screen, 50, 500) # old 300,200


        # Welcome message
        draw_text("Hello " + str(username) + "!", button_font, (0, 0, 0), screen, 525, 550)

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

# intent: Creates pause menu when the "esc" key is pressed
# Preconditions: All variables are assigned predetermined values to not cause error
# Postcondition: The "Pause screen" will show up on the users screen while in game
#                and allows for the user to do several operations if wanted.
def pause_game_screen(username = "", locations = [0,0], level_num="", score = ""):
    global Mute
    #Pause Menu image location and its rect
    myimage = pygame.image.load("images/pausemenu.png")
    imagerect = pygame.Rect(255, 215, 350, 240)
    click_sound = pygame.mixer.Sound('audio/click.wav')
    running = True
    click = False

    while running:
        
        #add image to screen
        screen.blit(myimage, imagerect)
        
        mx, my = pygame.mouse.get_pos()
        
        draw_text('PAUSED', font, (0, 0, 0), screen, 20, 50)

        # Creating the buttons
        continue_button = pygame.Rect(320, 246, 160, 25) # old 50,100,200,50
        save_button = pygame.Rect(310, 275, 175, 24) # old 50,100,200,50
        exit_button = pygame.Rect(350, 305, 88, 25) # old 50,100,200,50
        mute_button = pygame.Rect(285, 332, 88, 25) # old 50,100,200,50
        unmute_button = pygame.Rect(390, 332, 130, 25) # old 50,100,200,50

        player_rect = pygame.Rect(100, 100, 5, 13)

        if locations[0] == 0 and locations[1] == 0:
            pass
        else:
            player_rect.x = locations[0]
            player_rect.y = locations[1]   

        # Checking if the mouse click collides with the button
        if continue_button.collidepoint((mx, my)):
            if click:
                click_sound.play()
                return True

        if save_button.collidepoint((mx, my)):
            if click:
                click_sound.play()
                player_location = []
                player_location.append(int(player_rect.x))
                player_location.append(int(player_rect.y))  
                SaveGame(username, player_location, level_num, str(score))

                draw_text('SAVED!', title_font, black, screen, 285, 100)


        if exit_button.collidepoint((mx, my)):
            if click:
                click_sound.play()
                pygame.mixer.music.fadeout(1000)
                #get_score(str(score), username)
                main_menu(username)    
                return False

        if mute_button.collidepoint((mx, my)):
            if click:
                click_sound.play()
                Mute = True
                pygame.mixer.music.fadeout(1000)

        if unmute_button.collidepoint((mx, my)):
            if click:
                click_sound.play()
                Mute = False
                pygame.mixer.music.play(-1)           

               
        
        # Checks for mouse click
        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                 if event.key == K_ESCAPE:
                     return True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(60)

# Intent: Closes the game window
# Postcondition: Closes the game window (application closes)
def Exit():
    pygame.quit()
    sys.exit()

# Intent: Shows a GUI of the available levels that the player can play
# Precondition: username = a legal username that is given from
#               the login window when the user logs into their account
def LevelSelect(username):
    # click variable to detect when the user clicks a button
    click = False
    running = True
    while running:

        #screen.fill(Baby_Blue)
        screen.blit(ldr_image, (0, 0))

        draw_text('Level Select', font, black, screen, 20, 20)

        # gets the x and y positions of the mouse and puts them
        # into our variables mx, my
        mx, my = pygame.mouse.get_pos()

        # Creation of our buttons
        # x, y, length, height
        button_1 = pygame.Rect(50, 100, 160, 40) # old 50,100,150,50
        button_2 = pygame.Rect(50, 200, 160, 40) # old 50,200,150,50
        button_3 = pygame.Rect(50, 300, 160, 40) # old 50,300,150,50
        button_4 = pygame.Rect(50, 400, 160, 40) # old 300,100,150,50
        button_5 = pygame.Rect(50, 500, 160, 40) # old 300,200,150,50

        # checking for collisions
        if button_1.collidepoint((mx, my)):
            if click:
                location = [0,0]
                level1(location, username, '1')
        if button_2.collidepoint((mx, my)):
            if click:
                location = [0,0]
                level1(location, username, '2')
        if button_3.collidepoint((mx, my)):
            if click:
                location = [0,0]
                level1(location, username, '3')
        if button_4.collidepoint((mx, my)):
            if click:
                location = [0,0]
                level1(location, username, '4')
        if button_5.collidepoint((mx, my)):
            if click:
                location = [0,0]
                level1(location, username, '5')

        # renders the buttons
        #pygame.draw.rect(screen, (255,255,255), button_1)
        draw_text("Level 1", button_font, black, screen, 50, 100)

        #pygame.draw.rect(screen, (255,255,255), button_2)
        draw_text("Level 2", button_font, black, screen, 50, 200)

        #pygame.draw.rect(screen, (255,255,255), button_3)
        draw_text("Level 3", button_font, black, screen, 50, 300)

        #pygame.draw.rect(screen, (255,255,255), button_4)
        draw_text("Level 4", button_font, black, screen, 50, 400) # old 300,100

        #pygame.draw.rect(screen, (255,255,255), button_5)
        draw_text("Level 5", button_font, black, screen, 50, 500) # old 300,200

        # must reset the click variable before every event
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            # case when the user clicks onto a button
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                
            pygame.display.update()
            mainClock.tick(60) # framerate of the game

# Intent: Shows the user logged in the leaderboards for the entire game.
#         The leaderboards contains the top 5 players and their total scores.
def LeaderBoards():
     # click variable to detect when the user clicks a button
    click = False
    running = True

    f2 = open('accounts/leaderboard.txt', 'r')

    content = f2.readlines()
    f2.close()

    f = open('accounts/leaderboard.txt', 'r')

    name = []
    score = []

    length = len(content)
    length = length * 0.5
    loop = int(length)

    for i in range(loop):
        name.append(f.readline())
        score.append(f.readline())

    while running:

        screen.blit(ldr_image, (0, 0))
        draw_text('Leaderboards', title_font, black, screen, 136, 20)

        mainWindow = pygame.Rect(150, 35, 300, 240)

        # gets the x and y positions of the mouse and puts them
        # into our variables mx, my
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(175, 50, 150, 50)

        # Drawing the leaderboards onto the screen
        names1 = name[0]
        name1 = names1[:len(names1) - 1]
        scores1 = score[0]
        score1 = scores1[:len(scores1) - 1]

        draw_text("1. " + name1, button_font, black, screen, 136, 150) # old 175,50
        draw_text(score1, button_font, black, screen, 540, 150)


        button_2 = pygame.Rect(175, 90, 150, 50)

        names2 = name[1]
        name2 = names2[:len(names2) - 1]
        scores2 = score[1]
        score2 = scores2[:len(scores2) - 1]
        draw_text("2. " + name2, button_font, black, screen, 136, 200) # old 175,50
        draw_text(score2, button_font, black, screen, 540, 200)


        names3 = name[2]
        name3 = names3[:len(names3) - 1]
        scores3 = score[2]
        score3 = scores3[:len(scores3) - 1]
        draw_text("3. " + name3, button_font, black, screen, 136, 250) # old 175,50
        draw_text(score3, button_font, black, screen, 540, 250)


        names4 = name[3]
        name4 = names4[:len(names4) - 1]
        scores4 = score[3]
        score4 = scores4[:len(scores4) - 1]
        draw_text("4. " + name4, button_font, black, screen, 136, 300) # old 175,50
        draw_text(score4, button_font, black, screen, 540, 300)


        names5 = name[4]
        name5 = names5[:len(names5) - 1]
        scores5 = score[4]
        score5 = scores5[:len(scores5) - 1]
        draw_text("5. " + name5, button_font, black, screen, 136, 350) # old 175,50
        draw_text(score5, button_font, black, screen, 540, 350)


        # must reset the click variable before every event
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            # case when the user clicks onto a button
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            mainClock.tick(60)  # Framerate of the game

# Intent: this function allows for me to save a game while playing
# Preconditions: user = "". holds the users username
#                location = [0,0]. Holds the users location
#                level = "". Holds the level of the player
# Poscondition: the game is saved to a file
def SaveGame(user = "", location = [0,0], level="", score = ""):
    # open a file named the username.
    # If the file does not exist it will create it
    # If the file already exists, it truncates the previous version
    f = open("accounts/savefiles/" + user + ".txt", "w+")
    # Storing the values of the player position
    x = str(location[0])
    y = str(location[1])

    f.write(x+','+y+','+level)

    f.close()

    get_score(score, user)


# Intent: This helper function allows for the programmer to load a game
# Precondition: user = "", default case in case the programmer by accident forgets
#               to pass the username.
def LoadGame(user = ""):

    #checks to see if fileexists
    fileexists = path.exists("accounts/savefiles/" + user + ".txt")

    if fileexists:
        f = open("accounts/savefiles/" + user + ".txt", "r+")
        contents = f.read()

        text = contents.split(',')

        # getting the location of the player
        location = []
        location.append(int(text[0]))
        location.append(int(text[1]))

        #Getting the level the player saved in
        level = int(text[2])

        if level == 1:
            level1(location, user, '1')
        elif level == 2:
            level1(location, user, '2')
        elif level == 3:
            level1(location, user, '3')
        elif level == 4:
            level1(location, user, '4')
        elif level == 5:
            level1(location, user, '5')
    else:
        location = [0,0]
        level1(location, user, '1')



# Intent: Helper function that tests for collisions of the player
# Postconditions: Gives the main game loop the collisions that are currently happening
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

# Intent: Helper function to make sure that when the user moves they are colliding with the correct
#         "tiles"
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

# Intent: Helper function to load in the character animations
# Preconditions: path, frame_durations are always passed legal values that correspond
#                to each of the specific animations for the character
# Postcondition: returns the animation frame the character is currently in
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

# Intent: Helper function that helps the programmer transition the players current animations
# Preconditions: action_var = the previous action the player is doing
#                new_value = the current action the player is doing
#                frame = the frame the animation is currently in
#
# Postcondition: Returns the animation the player is currently in and the frame that animation is in
def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var,frame

# Intent: Once the user reaches the end of a level a "Continue screen" is prompted.
#         The continue screen allows for the player to continue to the next level or exit the game and return to the main menu
#
# Preconditions: All variables are passed legal values (this has been thoroughly tested)
def continue_screen(username, level, score):
    # click variable to detect when the user clicks a button
    click = False
    running = True
    while running:

        #screen.fill(Baby_Blue)
        screen.blit(ldr_image, (0, 0))

        draw_text('Continue Screen', font, black, screen, 20, 20)

        # gets the x and y positions of the mouse and puts them
        # into our variables mx, my
        mx, my = pygame.mouse.get_pos()

        # Creation of our buttons
        # x, y, length, height
        button_1 = pygame.Rect(50, 100, 160, 40) # old 50,100,150,50
        button_2 = pygame.Rect(50, 200, 160, 40) # old 50,200,150,50

        # checking for collisions
        if button_1.collidepoint((mx, my)):
            if click:
                location = [0,0]
                if level == '1':
                    get_score(score, username)
                    level1(location, username, '2')
                elif level == '2':
                    get_score(score, username)
                    level1(location, username, '3')
                elif level == '3':
                    get_score(score, username)
                    level1(location, username, '4')
                elif level == '4':
                    get_score(score, username)
                    level1(location, username, '5')
        if button_2.collidepoint((mx, my)):
            if click:
                if level == '1':
                    SaveGame(username, [0,0], '2', score)
                    main_menu(username)
                elif level == '2':
                    SaveGame(username, [0,0], '3', score)
                    main_menu(username)
                elif level == '3':
                    SaveGame(username, [0,0], '4', score)
                    main_menu(username)
                elif level == '4':
                    SaveGame(username, [0,0], '5', score)
                    main_menu(username)

        # renders the buttons
        #pygame.draw.rect(screen, (255,255,255), button_1)
        draw_text("Continue", button_font, black, screen, 50, 100)

        #pygame.draw.rect(screen, (255,255,255), button_2)
        draw_text("Exit", button_font, black, screen, 50, 200)

        # must reset the click variable before every event
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            # case when the user clicks onto a button
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                
            pygame.display.update()
            mainClock.tick(60) # framerate of the game

# Intent: Displays to the user the end screen for beating the game
# Precondition: The parameters passed are legal (This has been tested thoroughly)
def end_screen(username, score):
    # click variable to detect when the user clicks a button
    click = False
    running = True
    while running:

        #screen.fill(Baby_Blue)
        screen.blit(ldr_image, (0, 0))

        draw_text('End of Game', font, black, screen, 20, 20)
        draw_text("Congratulations for beating", button_font, black, screen, 50, 100)
        draw_text("the game!", button_font, black, screen, 50, 150)

        # gets the x and y positions of the mouse and puts them
        # into our variables mx, my
        mx, my = pygame.mouse.get_pos()

        # Creation of our buttons
        # x, y, length, height
        button_1 = pygame.Rect(50, 250, 160, 40) # old 50,100,150,50

        # checking for collisions
        if button_1.collidepoint((mx, my)):
            if click:
                get_score(score, username)
                main_menu(username)

        # renders the buttons
        #pygame.draw.rect(screen, (255,255,255), button_1)
        draw_text("Exit", button_font, black, screen, 50, 250)

        # must reset the click variable before every event
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # case when the user clicks onto a button
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                
            pygame.display.update()
            mainClock.tick(60) # framerate of the game

# Intent: When the user falls off the map this screen pops up
#         prompting the user if they want to continue or exit to the main menu
# Preconditions: User has fallen off the map
# Postconditions: User restarts level or returns to the main menu
def death_screen(username, level, score):
    # click variable to detect when the user clicks a button
    click = False
    running = True
    while running:

        #screen.fill(Baby_Blue)
        screen.blit(ldr_image, (0, 0))

        draw_text('Death Screen', font, black, screen, 20, 20)
        draw_text("You died!", button_font, black, screen, 50, 100)

        # gets the x and y positions of the mouse and puts them
        # into our variables mx, my
        mx, my = pygame.mouse.get_pos()

        # Creation of our buttons
        # x, y, length, height
        button_1 = pygame.Rect(50, 200, 160, 40) # old 50,100,150,50
        button_2 = pygame.Rect(50, 250, 160, 40) # old 50,200,150,50

        # checking for collisions
        if button_1.collidepoint((mx, my)):
            if click:
                get_score(score, username)
                location = [0,0]
                if level == '1':
                    level1(location, username, '1')
                elif level == '2':
                    level1(location, username, '2')
                elif level == '3':
                    level1(location, username, '3')
                elif level == '4':
                    level1(location, username, '4')
                elif level == '5':
                    level1(location, username, '5')
        if button_2.collidepoint((mx, my)):
            if click:
                get_score(score, username)
                main_menu(username)

        # renders the buttons
        #pygame.draw.rect(screen, (255,255,255), button_1)
        draw_text("Restart Level", button_font, black, screen, 50, 200)

        #pygame.draw.rect(screen, (255,255,255), button_2)
        draw_text("Exit", button_font, black, screen, 50, 250)

        # must reset the click variable before every event
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            # case when the user clicks onto a button
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                
            pygame.display.update()
            mainClock.tick(60) # framerate of the game


# Intent: Return a random RGB color from 0 - 255
# Postcondition: The function returns a color value between 0 - 255
def random_color():
    random_color_value = random.randrange(35, 255, 3)
    return random_color_value


# Intent: Create the level based on the parameters based
# Preconditions: locations = [0,0] location of the player
#                username = "" name of the player
#                level_num = '1' the level we are supposed to load
#                All preconditions are intentionally pre given values just in case
#                a programmer forgets to pass the function paramters. (will start at level 1)
def level1(locations = [0,0], username = "", level_num = '1'):

    # Keeps track of the players score
    score = 10000

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
    game_map = load_map('maps/map'+level_num)

    grass_image = pygame.image.load('images/grass.png')
    TILE_SIZE = grass_image.get_width()
    dirt_image = pygame.image.load('images/dirt.png')

    # Sounds
    global Mute
    jump_sound = pygame.mixer.Sound('audio/jump.wav')
    grass_sounds = [pygame.mixer.Sound('audio/grass_0.wav'),pygame.mixer.Sound('audio/grass_1.wav')]
    grass_sounds[0].set_volume(0.2)
    grass_sounds[1].set_volume(0.2)
    if Mute == False:
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

    true_scroll = [] # NOTE: This was changed from -> [0,0]
    true_scroll.append(locations[0])
    true_scroll.append(locations[1])

    # Collision!, [left(x), top(y), width, height]
    player_rect = pygame.Rect(100, 100, 5, 13)

    if locations[0] == 0 and locations[1] == 0:
        pass
    else:
        player_rect.x = locations[0]
        player_rect.y = locations[1]


    rand_color_1 = random_color()
    rand_color_2 = random_color()
    rand_color_3 = random_color()
    rand_color_4 = random_color()
    rand_color_5 = random_color()
    rand_color_6 = random_color()
    rand_color_7 = random_color()
    rand_color_8 = random_color()
    rand_color_9 = random_color()

    running = True
    while running:

        # While the player is alive their score will be 
        # incrementing by 5's
        if score > 0:
            score -= 1

        # red, green, blue
        # display.fill((146,244,255))
        display.fill((rand_color_1,rand_color_2,rand_color_3))
               
        if grass_sound_timer > 0:
            grass_sound_timer -= 1

        # Camera following player
        true_scroll[0] += (player_rect.x - true_scroll[0] - 152)/20
        true_scroll[1] += (player_rect.y - true_scroll[1] - 106)/20

        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        # rand_color_
        pygame.draw.rect(display, (rand_color_1, rand_color_2, rand_color_3), pygame.Rect(0,120,300,80))
        for background_object in background_objects:
            obj_rect = pygame.Rect(background_object[1][0] - scroll[0]*background_object[0], background_object[1][1] - scroll[1]*background_object[0], background_object[1][2], background_object[1][3])
            if background_object[0] == 0.5:
                pygame.draw.rect(display, (rand_color_4, rand_color_5,rand_color_6),obj_rect) # rendering the object a certain value based on its scroll multiplier
            else:
                pygame.draw.rect(display, (rand_color_7, rand_color_8, rand_color_9),obj_rect)



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
        player_movement = [0,0] # NOTE: This was changed from -> [0,0]
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
        
        # Rendering the score onto the screen
        score_text = font2.render("Score: " + str(score), True, black)
        display.blit(score_text, (0, 0) )

        # Catches what buttons the player presses and performs those actions
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    pygame.mixer.music.fadeout(1000)
                if event.key == K_s:
                    player_location = []
                    player_location.append(int(player_rect.x))
                    player_location.append(int(player_rect.y))
                        
                    SaveGame(username, player_location, level_num, str(score))
                if event.key == K_e:
                    pygame.mixer.music.play(-1)
                if event.key == K_RIGHT:
                    moving_right = True
                    score += 2
                if event.key == K_ESCAPE:

                    player_location = []
                    player_location.append(int(player_rect.x))
                    player_location.append(int(player_rect.y))

                    pause_game_screen(username, player_location, level_num, str(score))

                    # fixing moving on own bug
                    moving_right = False
                    moving_left = False


                if event.key == K_LEFT:
                    moving_left = True
                    score += 2
                if event.key == K_UP:
                    score += 5
                    if air_timer < 6:
                        jump_sound.play()
                        player_y_momentum = -5
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False

        
        # This if-elif tree checks to
        # see if the user has reached the end of the level they are in
        # IF they reached the end of the level we call the continue screen
        # This branch also checks to see if the player fell off the map
        if level_num == '1':
            if player_rect.x >= 2271 and player_rect.y == 131:
                pygame.mixer.music.fadeout(1000)
                continue_screen(username, level_num, str(score))
            elif player_rect.y >= 226:
                pygame.mixer.music.fadeout(1000)
                death_screen(username, level_num, score)
        elif level_num == '2':
            if player_rect.x >= 4721 and player_rect.y == 99:
                pygame.mixer.music.fadeout(1000)
                continue_screen(username, level_num, str(score))
            elif player_rect.y >= 333:
                pygame.mixer.music.fadeout(1000)
                death_screen(username, level_num, score)
        elif level_num == '3':
            if player_rect.x >= 4557 and player_rect.y == 67:
                pygame.mixer.music.fadeout(1000)
                continue_screen(username, level_num, str(score))
            elif player_rect.y >= 333:
                pygame.mixer.music.fadeout(1000)
                death_screen(username, level_num, score)
        elif level_num == '4':
            if player_rect.x >= 4741 and player_rect.y == 291:
                pygame.mixer.music.fadeout(1000)
                continue_screen(username, level_num, str(score))
            elif player_rect.y >= 333:
                pygame.mixer.music.fadeout(1000)
                death_screen(username, level_num, score)
        elif level_num == '5':
            if player_rect.x >= 4699 and player_rect.y == 35:
                pygame.mixer.music.fadeout(1000)
                end_screen(username, str(score))
            elif player_rect.y >= 333:
                pygame.mixer.music.fadeout(1000)
                death_screen(username, level_num, score)
            
        
        # changes the size of my smaller image to be the size
        # of the new image
        surf = pygame.transform.scale(display, res)
        screen.blit(surf, (0, 0))

        pygame.display.update()
        mainClock.tick(60)
    pygame.mixer.music.fadeout(500)


# Intent: This function is supposed to get the users score and update their total score 
#         in the game. It then will update leaderboard.txt and make sure the top 5 players
#         are in correct order.
# Preconditions: score, holds the user score
#                username, holds the name of the player
# Postconditions: score will be added to the score.txt file along with its respective user
def get_score(score, username):
    found = False

    f2 = open('accounts/scores.txt', 'r')

    content = f2.readlines()
    f2.close()

    f = open('accounts/scores.txt', 'r')

    name = []
    scores = []

    length = len(content)
    length = length * 0.5
    loop = int(length)

    for i in range(loop):
        name.append(f.readline())
        scores.append(f.readline())

    # Finds the user in the name array, if the user exists we then
    # add their new score to their total score.
    for i in range(len(name)):
        if name[i] == username+"\n":
            found = True
            string = scores[i]
            actual_score = string[:len(string) - 1]

            points = int(actual_score)
            points += int(score)

            scores[i] = str(points)
            scores[i] += "\n"

            f.close()
    
    f.close()

    # Rewriting scores.txt file with the updated scores.txt
    f3 = open('accounts/scores.txt', 'w')
    for i in range(loop):
        f3.write(name[i])
        f3.write(scores[i])
    f3.close()

    # If the user was found we update the leaderboards()
    if found:
        update_leaderboards()
    else:
        # This is the case when the user was not found.
        # in that case we just append their username and score to scores.txt
        f2 = open('accounts/scores.txt', 'a')
        f2.write(str(username) + "\n" )
        f2.write(str(score) + "\n")
        f2.close()
        update_leaderboards()


# Intent: This function updates the leaderboard.txt file
#         to have the current high scores of the game based on account
def update_leaderboards():
    f2 = open('accounts/scores.txt', 'r')

    content = f2.readlines()
    f2.close()

    f = open('accounts/scores.txt', 'r')

    name = []
    score = []

    length = len(content)
    length = length * 0.5
    loop = int(length)

    for i in range(loop):
        name.append(f.readline())
        score.append(f.readline())

    f.close()

    print(score)

    # Bubble sort the score array
    for i in range(loop - 1):
        for j in range(loop - i - 1):
            first_score = score[j]
            score1 = int(first_score[:len(first_score) - 1])

            second_score = score[j+1]
            score2 = int(second_score[:len(second_score) - 1])
            if score1 < score2:
                score[j], score[j+1] = score[j+1], score[j]
                name[j], name[j+1] = name[j+1], name[j]
    
    f3 = open("accounts/leaderboard.txt", "w")

    # Adding the top 5 scores into leaderboard.txt
    if loop < 5:
        for l in range(len(score)):
            f3.write(str(name[l]))
            f3.write(str(score[l]))
    else:
        for f in range(5):
            f3.write(str(name[f]))
            f3.write(str(score[f]))

