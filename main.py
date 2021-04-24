import UserLogin
#import Game

# call the user login window
UserLogin.log_in_win()

# Then grab the username if the user logged in
player = str(UserLogin.get_user_name())

# If the player just exited the login window then the "get_user_name()" will return 
# an empty string indicating that the user did not log in but instead closed the window
if player == "":
    exit()
else:
    # Else the user logged in and we pass their name
    import Game
    Game.main_menu(player)