## This is a comment to see if everything is working correctly
## test commit joe
import UserLogin
import Game

UserLogin.log_in_win()

name = str(UserLogin.get_user_name())

if name == "":
    exit()
else:
    Game.main_menu(name)